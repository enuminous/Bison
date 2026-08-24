from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Component:
    capacity: float
    queue_limit: float
    criticality: float = 1.0
    priority: int = 1
    retry_fraction: float = 0.0
    queue: float = 0.0

class BisonSystem:
    def __init__(self, components: Dict[str, Component], critical_latency_limit: float = 2.0):
        self.components = components
        self.critical_latency_limit = critical_latency_limit
        self.time = 0

    def step(self, demand: Dict[str, float]):
        result = {}
        total_viol = 0
        weighted_viol = 0.0
        total_weight = 0.0

        retry_injections = {k:0.0 for k in self.components}

        for name,c in self.components.items():
            d = max(0.0, demand.get(name,0.0)) + retry_injections.get(name,0.0)
            available = max(0.0, c.capacity)
            served = min(d + c.queue, available)
            new_queue = max(0.0, c.queue + d - served)
            dropped = max(0.0, new_queue - c.queue_limit)
            new_queue = min(new_queue, c.queue_limit)
            c.queue = new_queue

            pressure = d/(available+1e-9) if available > 0 else float("inf")
            latency_proxy = 1.0 + (c.queue/(available+1e-9))
            queue_violation = c.queue >= c.queue_limit and c.queue_limit > 0
            latency_violation = c.criticality >= 1.0 and latency_proxy > self.critical_latency_limit

            violations = int(queue_violation) + int(latency_violation)
            total_viol += violations
            total_weight += 2.0*c.criticality
            weighted_viol += c.criticality*violations

            retry = dropped*c.retry_fraction

            result[name] = {
                "demand": d,
                "served": served,
                "queue": c.queue,
                "dropped": dropped,
                "retry_generated": retry,
                "pressure": pressure,
                "latency_proxy": latency_proxy,
                "violations": violations
            }

        integrity = 1.0
        if total_weight > 0:
            integrity = max(0.0, 1.0 - weighted_viol/total_weight)

        critical_loss = 0.0
        total_loss = 0.0
        for name,r in result.items():
            loss = r["dropped"]
            total_loss += loss
            critical_loss += loss*self.components[name].criticality

        graceful = 1.0
        if total_loss > 0:
            graceful = max(0.0, 1.0 - critical_loss/(total_loss + 1e-9))

        self.time += 1
        return {
            "time": self.time,
            "components": result,
            "boundary_integrity": integrity,
            "total_violations": total_viol,
            "graceful_degradation": graceful,
        }
