# Overload Model

## Component schema

```json
{
  "name": "api",
  "capacity": 100,
  "criticality": 1.0,
  "queue_limit": 200,
  "priority": 1
}
```

## State

For each component:
- demand
- capacity
- queue
- served work
- dropped work
- retries
- boundary violations

## Pressure

`pressure = demand / capacity`

## Queue update

`queue_next = max(0, queue + demand - served)`

## Drop condition

If:

`queue_next > queue_limit`

then excess work is dropped.

## Retry amplification

`retry_load = retry_fraction * dropped_work`

which may be routed to the same or another subsystem.

## Boundary examples

- latency must remain below a critical ceiling
- one tenant may not consume more than an isolation share
- reserved capacity must remain available to safety-critical traffic
- memory reserve may not fall below a minimum

## Graceful degradation test

Under increasing demand, BISON records the order in which:
1. optional throughput declines
2. noncritical queues saturate
3. critical latency degrades
4. hard boundaries are violated

A safer system fails in roughly that order.
