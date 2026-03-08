# Project Progress

## Goal
Track implementation progress for Stage 1 of the Spatial Economic Field model.

## Status Legend
- `TODO`: not started
- `IN_PROGRESS`: currently working on it
- `DONE`: implemented and sanity-checked

## Stage 1 Milestones

1. `IN_PROGRESS` Milestone A: Data model and initialization
- [ ] Define parameters (`Lx`, `Ly`, `p_init`, `M0`, `P`, `K`, `C`, `lambda`)
- [ ] Create occupancy grid initialization from `p_init`
- [ ] Create money grid initialization (`M0` where occupied, else `0`)
- [ ] Print/check initial firm count and total initial money
- [ ] Run one reproducible initialization with fixed seed

2. `TODO` Milestone B: Distance and delivered price
- [ ] Implement Manhattan distance
- [ ] Implement delivered price formula
- [ ] Verify with 2-3 hand-checked examples

3. `TODO` Milestone C: One-step demand allocation with capacity
- [ ] Supplier choice per demand cell
- [ ] Capacity constraints
- [ ] Track units sold per firm

4. `TODO` Milestone D: Money update and firm death
- [ ] Revenue update
- [ ] Survival cost update
- [ ] Death/removal when money < 0

5. `TODO` Milestone E: Full simulation loop
- [ ] Multi-step run
- [ ] Per-step metrics collection

6. `TODO` Milestone F: Experiment sweep on `lambda`
- [ ] Low/medium/high lambda setup
- [ ] Multiple seeds per condition
- [ ] Aggregate and compare outputs

7. `TODO` Milestone G: Visualization and interpretation
- [ ] Final occupancy map
- [ ] Surviving firms over time plot
- [ ] Concentration comparison across lambda

## Session Log
- 2026-03-08: Created progress tracker and started Milestone A.
