# BISON — EFMW Zoo #31

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
