# BISON — EFMW Zoo #31

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Bison) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Boundary Integrity and Systemic Overload Network**

BISON is an experimental EFMW-inspired framework for evaluating whether a system preserves critical boundaries under overload, contention, resource exhaustion, and cascading pressure.

## Core question

> When the system is pushed beyond comfortable operating conditions, what fails first: performance, isolation, policy boundaries, or system integrity?

BISON is designed to distinguish graceful degradation from boundary collapse.

## Primary outputs

- overload pressure
- boundary violation count
- isolation integrity
- contention amplification
- graceful-degradation score
- saturation onset
- recovery lag
- overload cascade risk

## Repository contents

- `theory.md`
- `architecture.md`
- `overload_model.md`
- `limitations.md`
- `bison.py`
- `benchmark.py`
- `ablations.py`
- `test_bison.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_bison.py
```

## Zoo position

MANTIS #30 watches for nonlinear transitions.

**BISON #31 tests whether system boundaries survive when pressure actually arrives.**
