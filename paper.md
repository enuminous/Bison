# BISON: Boundary Integrity and Systemic Overload Network

## Abstract

BISON is an experimental framework for evaluating system behavior under overload, contention, queue saturation, and resource exhaustion. Unlike ordinary load testing, BISON explicitly measures which boundaries are sacrificed as pressure increases and whether degradation remains confined to lower-priority service.

## 1. Motivation

High utilization is not itself the core failure.

The more important question is whether overload causes:
- boundary violations,
- isolation loss,
- critical service degradation,
- retries and amplification,
- prolonged recovery.

## 2. Model

Resource pressure:

`p_r=d_r/c_r`

Queue dynamics:

`q(t+1)=max(0,q(t)+arrivals-service)`

Boundary integrity:

`I=1-weighted_violation_fraction`

Graceful degradation:

`G=1-critical_loss/(total_loss+eps)`

## 3. Metrics

- saturation onset
- queue growth
- dropped work
- boundary-integrity score
- critical versus noncritical loss
- retry amplification
- recovery lag

## 4. Baselines

- conventional load testing
- queueing models
- SRE saturation metrics
- stress testing
- chaos engineering
- capacity planning

## 5. Ablations

- remove boundary scoring
- remove queue limits
- remove criticality weighting
- remove retry modeling
- remove recovery tracking
- equalize traffic priorities

## 6. Falsification

If conventional load tests and queueing metrics capture the same operational failures with equal clarity and predictive value, BISON's added structure is not justified.

## 7. Claim boundary

BISON is a systems stress-evaluation framework. Synthetic overload results do not establish production resilience.
