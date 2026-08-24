# Limitations and Falsification

BISON is an experimental overload and boundary-integrity framework.

## Limitations

- Capacity estimates may be wrong.
- Synthetic load may not match production traffic.
- Queue models may oversimplify real schedulers.
- Retry behavior can be workload-specific.
- Some boundary violations are difficult to observe.
- Priority definitions can encode subjective choices.

## Falsification criteria

BISON's central hypothesis is weakened if:

1. Conventional load tests capture the same boundary failures.
2. Boundary scoring adds no predictive value.
3. Retry amplification modeling does not improve cascade prediction.
4. Graceful-degradation metrics fail to correlate with real incidents.
5. Results do not generalize across traffic shapes.
6. Recovery tracking adds no operational information.

## Claim boundary

BISON evaluates overload behavior under specified capacities, demand, and boundaries. It does not guarantee resilience under unseen workloads.
