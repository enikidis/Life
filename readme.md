# Spatial Economic Field Model

## 1. Context and Goal
This project started from a Game of Life intuition: simple local rules can create complex global patterns.

In Stage 1, we translate that idea into an economic grid model and test one focused hypothesis:

When transport cost (`lambda`) increases, surviving firms become more spatially concentrated (hub formation).

## 2. Stage 1 Scope (What Is In / Out)
Stage 1 is intentionally minimal so results are interpretable.

Included:
- Spatial grid
- Firms with simple accounting
- Demand at every location
- Distance-based transport penalty
- Entry only at initialization, exit by bankruptcy

Not included (for now):
- Individuals/workers
- Firms formed by neighboring cells
- Productivity spillovers/agglomeration bonuses
- Multi-good production chains
- Explicit transport agents or logistics networks

## 3. World Definition
- The world is a 2D grid of size `Lx x Ly`.
- Each cell is a demand location.
- A cell may contain at most one firm.
- There is one homogeneous good.
- Demand is fixed at 1 unit per cell per step.

## 4. Entities and State Variables
### Firm
Each firm has:
- `location (x, y)`
- `money`
- `capacity` (max units sold per step)
- `price` (base price per unit)

### World fields
- `occupancy[x, y]`: whether a firm exists in the cell
- `money[x, y]`: current money of firm in that cell (0 if empty)
- `demand[x, y]`: fixed to 1 in Stage 1

## 5. Parameters
- `Lx, Ly`: grid size
- `p_init`: probability a cell starts with a firm
- `M0`: initial money per firm
- `P`: base selling price
- `K`: production/sales capacity per step
- `C`: survival cost per step
- `lambda`: transport cost coefficient
- `distance_metric`: Manhattan distance (Stage 1 default)

## 6. Initialization
At `t = 0`:
1. Create the grid.
2. Place firms independently with probability `p_init`.
3. Assign `M0` to occupied cells and `0` to empty cells.
4. Keep all cells as demand cells (`demand = 1`).

## 7. Step Dynamics
Each simulation step runs in this order:

1. Production availability
- Every active firm can sell up to `K` units.

2. Supplier choice by each demand cell `j`
- Evaluate each active firm `i` with:
  `delivered_price(i, j) = P + lambda * distance(i, j)`
- Choose the firm with the lowest delivered price.
- Ties: break randomly (or by fixed deterministic rule, but keep it constant across runs).

3. Sales under capacity constraint
- A firm serves assigned buyers until reaching `K` units.
- Unserved demand is lost for that step.

4. Revenue update
- For each firm:
  `money = money + P * units_sold`

5. Survival cost
- For each firm:
  `money = money - C`

6. Death
- If `money < 0`, remove the firm:
  - `occupancy = 0`
  - `money = 0`

## 8. Measurement Outputs
Track at least:
- Number of surviving firms over time
- Firm-level sales distribution
- Average transport distance per unit sold
- Spatial concentration metrics:
  - Top-k sales share
  - Optional Gini-like concentration index
  - Optional cluster-size distribution

## 9. Experiment Protocol
Run many simulations while varying only `lambda`:
- low `lambda`
- medium `lambda`
- high `lambda`

Keep all other parameters fixed and random seed policy explicit.

Compare outcomes across conditions to test whether higher `lambda` increases concentration/hub dominance.

## 10. Coherent End Plan
### Phase A: Minimal engine
- Grid + initialization
- One-step demand allocation with capacity
- Money update + death

### Phase B: Repeatable experiments
- Multi-step simulation loop
- Batch runs across `lambda`
- Save summary statistics per run

### Phase C: Analysis and visualization
- Time series: surviving firms
- Maps of final firm distribution
- Concentration plots vs `lambda`

### Phase D: Interpretation
- Decide if evidence supports the hypothesis:
  higher `lambda` -> stronger spatial concentration.

### Phase E: Optional Stage 2 extensions
Only after Stage 1 is validated:
- Agglomeration/productivity effects
- Delayed insolvency / credit buffer
- Multiple goods or dependencies
- Richer transport structure

## 11. Learning-First Workflow
Because this is a Python learning project:
- Implement one small milestone at a time.
- Test each milestone before adding complexity.
- Keep functions short and explicit.
- Prefer clarity over optimization in Stage 1.
