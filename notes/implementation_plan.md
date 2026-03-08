# Implementation Plan: From Game of Life to Spatial Economic Field (Stage 1)

## 1. Current Code Review (What you already have)

### `game_of_life/grid.py`
- `make_random_grid(...)`: creates random 0/1 occupancy grids.
- `make_glider(...)`: creates a classic GoL pattern.

Status for new project:
- Random initialization logic is reusable (conceptually) for firm placement with `p_init`.
- Glider logic is not needed for Stage 1 economic model.

### `game_of_life/rules.py`
- `count_neighbors(...)`: 8-neighborhood counting with wrap-around.
- `step(...)`: Conway update rule.

Status for new project:
- Not directly reusable for Stage 1 (economic dynamics are different).
- Useful as reference for array-based updates and clean function boundaries.

### `game_of_life/viz.py`
- `run_popup(...)`: interactive visualization loop.

Status for new project:
- Visualization loop style is reusable.
- Rendering logic must change (show firms/sales/money maps, not live/dead cells).

### `game_of_life/main.py`
- Creates initial grid and runs animation loop.

Status for new project:
- Control flow is reusable: initialize -> iterate -> display.
- Parameters and step function must be replaced by economic model.

## 2. Core Gap vs New `readme.md`

You currently have a cellular automaton engine.
You need an economic simulation engine with:
- Firm money and capacity,
- Demand assignment by delivered price,
- Revenue and survival cost,
- Firm death by bankruptcy,
- Experiment sweeps over `lambda`.

## 3. Stage 1 Build Plan (Detailed, learning-first)

## Milestone A: Data model and initialization
Goal: represent the economic world state cleanly.

Implement:
- Grid dimensions: `Lx, Ly`
- `occupancy` array (firm present: 0/1)
- `money` array (float or int)
- Uniform demand (implicitly 1 per cell; no need for separate array yet)
- Parameter container (dict or dataclass)
- Initialization function:
  - sample occupancy with `p_init`
  - set `money = M0` where occupied else 0

Done criteria:
- You can print number of initial firms and total initial money.

## Milestone B: Distance and delivered price
Goal: compute transport-aware effective prices.

Implement:
- Manhattan distance function between two cells.
- Delivered price formula:
  - `P + lambda * distance`

Done criteria:
- For test coordinates, delivered price matches manual calculation.

## Milestone C: One-step demand allocation with capacity
Goal: each demand cell chooses cheapest supplier.

Implement:
- For each demand cell:
  - evaluate delivered price from all active firms
  - choose cheapest (fixed tie-break rule)
- Capacity constraint:
  - each firm can serve at most `K` units
  - unmet demand is lost
- Track `units_sold` per firm

Done criteria:
- Total units sold <= number of demand cells
- No firm sells above `K`

## Milestone D: Money update and firm death
Goal: apply accounting and survival logic.

Implement:
- Revenue update: `money += P * units_sold`
- Survival cost: `money -= C`
- Death rule:
  - if `money < 0`, set occupancy to 0 and money to 0

Done criteria:
- Number of firms can decrease over time.
- Dead firms never sell next step.

## Milestone E: Full simulation loop
Goal: run many steps and collect basic outputs.

Implement:
- `run_simulation(T, params, seed)`
- Per-step metrics:
  - surviving firm count
  - total units sold
  - average transport distance

Done criteria:
- One run produces a structured results object (dict/dataframe-ready).

## Milestone F: Experiment sweep on `lambda`
Goal: test core hypothesis.

Implement:
- Choose low / medium / high `lambda`
- Multiple seeds per `lambda`
- Aggregate metrics by `lambda`

Done criteria:
- Table/summary shows how concentration changes with `lambda`.

## Milestone G: Visualization for interpretation
Goal: see spatial concentration directly.

Implement:
- Final occupancy heatmap
- Surviving firms over time plot
- Optional concentration metric plot vs `lambda`

Done criteria:
- You can visually compare low vs high `lambda` outcomes.

## 4. Suggested File Responsibilities

- `game_of_life/grid.py`
  - keep for initialization helpers or rename later to economic naming.
- `game_of_life/rules.py`
  - replace Conway rules with economic step logic.
- `game_of_life/main.py`
  - orchestrate parameters, run simulation, run experiments.
- `game_of_life/viz.py`
  - plotting and map/time-series visualizations.

Optional cleaner refactor later:
- `model/init.py`, `model/step.py`, `model/metrics.py`, `model/experiments.py`

## 5. Implementation Order (strict)

1. Milestone A
2. Milestone B
3. Milestone C
4. Milestone D
5. Milestone E
6. Milestone F
7. Milestone G

Do not skip ahead. Each milestone should run before starting the next.

## 6. Test Checklist per Milestone

- Fixed random seed for reproducibility.
- Small grid first (e.g., 10x10) for debugging.
- Print sanity checks:
  - number of firms,
  - total money,
  - max/min units sold,
  - count of dead firms per step.
- Only scale to larger grids after correctness checks pass.

## 7. Common Pitfalls to Avoid

- Mixing x/y and row/col indexing.
- Forgetting to exclude dead firms from supplier choice.
- Breaking capacity constraints during allocation.
- Changing multiple parameters while testing `lambda` effect.
- Adding Stage 2 mechanisms too early.

## 8. Definition of Stage 1 Success

You are done with Stage 1 when:
- The model runs end-to-end for multiple seeds,
- `lambda` is the only varied parameter,
- You can show whether higher `lambda` increases spatial concentration,
- Results are reproducible and interpretable.
