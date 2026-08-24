# BISON Architecture

## Pipeline

1. Demand Ingestor
2. Resource Meter
3. Saturation Detector
4. Queue/Contention Model
5. Boundary Evaluator
6. Retry Amplification Analyzer
7. Graceful-Degradation Scorer
8. Recovery Tracker
9. Overload Cascade Reporter

## Inputs

- resource capacities
- demand streams
- queue limits
- traffic priorities
- hard boundaries
- retry behavior
- dependency routing

## Outputs

```json
{
  "pressure": 1.24,
  "boundary_integrity": 0.88,
  "violations": 2,
  "graceful_degradation": 0.73,
  "retry_amplification": 1.41,
  "recovery_lag": 12
}
```

## Design principle

BISON distinguishes:
- degraded service
from
- degraded integrity.

Slower service may be acceptable.
Broken isolation or safety boundaries may not be.

## Integration

MANTIS can warn that the overload transition is approaching.

JELLYFISH can model downstream cascades.

BEAVER can evaluate overload mitigation.

WOLF can detect distributed pre-saturation signals.
