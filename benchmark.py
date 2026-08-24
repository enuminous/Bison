from bison import Component, BisonSystem

def run(multiplier):
    components = {
        "critical": Component(capacity=100, queue_limit=100, criticality=1.0, priority=1),
        "batch": Component(capacity=80, queue_limit=120, criticality=0.2, priority=3),
    }
    sys = BisonSystem(components, critical_latency_limit=1.8)
    outputs = []
    for _ in range(12):
        d = {
            "critical": 70*multiplier,
            "batch": 70*multiplier
        }
        outputs.append(sys.step(d))
    return {
        "multiplier": multiplier,
        "final_integrity": outputs[-1]["boundary_integrity"],
        "final_violations": outputs[-1]["total_violations"],
        "critical_queue": outputs[-1]["components"]["critical"]["queue"],
        "batch_queue": outputs[-1]["components"]["batch"]["queue"]
    }

if __name__ == "__main__":
    for m in [0.7,1.0,1.3,1.8]:
        print(run(m))
