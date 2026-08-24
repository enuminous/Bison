# BISON Theory

## 1. Problem

Systems under load can fail in more ways than simple slowdown.

Overload may cause:
- dropped work,
- queue explosion,
- latency spikes,
- resource starvation,
- isolation failure,
- cross-tenant interference,
- safety-boundary violations,
- retry storms,
- cascading saturation.

BISON treats overload as both a performance problem and a boundary-integrity problem.

## 2. Resource state

Let resource utilization be:

`u_r(t) in [0,1+]`

for resource `r`.

Examples:
- CPU
- memory
- bandwidth
- connection pool
- queue occupancy
- token budget
- worker capacity

## 3. Saturation pressure

For capacity `c_r` and demand `d_r`:

`p_r(t) = d_r(t) / (c_r + eps)`

Aggregate pressure:

`P_t = sum_r w_r * p_r(t)`

## 4. Boundary integrity

Let system constraints be:

`B_k(x_t) <= limit_k`

Boundary violation indicator:

`V_k(t) = 1[B_k(x_t) > limit_k]`

Boundary integrity score:

`I_t = 1 - weighted_violation_fraction`

## 5. Contention amplification

If subsystem `i` increases load on subsystem `j` through retries or backpressure:

`A_ij = downstream_load_increase / upstream_load_increase`

High `A_ij` indicates amplification.

## 6. Graceful degradation

Let ideal priority ordering be known.

A graceful system should sacrifice:
- low-priority throughput
before:
- critical correctness,
- safety boundaries,
- isolation.

Candidate degradation score:

`G = 1 - critical_loss / (total_loss + eps)`

Higher is better when losses are confined to noncritical service.

## 7. Recovery lag

After demand falls below capacity at `T_relief`:

`RecoveryLag = T_stable - T_relief`

Long lag may indicate queue poisoning, retry storms, or hysteresis.

## 8. Overload cascade

For components `i`:

`q_i(t+1) = max(0, q_i(t) + arrivals_i - service_i)`

Retries can make:

`arrivals_j += retry_rate_i * failures_i`

producing positive feedback.

## 9. EFMW interpretation

The EFMW-inspired element is recursive tracking of resource pressure, boundary state, contention relationships, and recovery through time.

The main relational question is not:

"Is utilization high?"

It is:

"Which boundaries are being traded away as pressure rises?"

## 10. Falsifiable prediction

BISON should add value where:
- multiple resources contend,
- overload causes policy/isolation failures,
- retries amplify demand,
- failure order matters,
- recovery exhibits hysteresis.

If standard load testing plus SRE saturation metrics capture all relevant failures, BISON's extra structure is not justified.
