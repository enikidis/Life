Here is a clean markdown summary of the plan so far. You can copy and save it.

---

# Spatial Economic Field – Stage 1 Plan

**Goal:** Show that transport constraints (λ) create spatial concentration (hubs).

---

## Core Idea

We build a minimal spatial economy on a grid.

We vary **λ (transport tightness)** and observe how economic activity distributes in space.

We keep everything else as simple as possible so that any hub formation can be attributed to transport costs.

---

## World Structure

* 2D grid (e.g. 50×50)
* Some squares contain firms
* All squares represent demand locations
* One single good exists

---

## Agent (Firm) Variables

Each firm has:

* `money`
* fixed `production capacity`
* fixed `price`
* fixed `survival cost`

No workers, no energy, no transport agents (yet).

---

## Transport Rule

Delivered price from firm *i* to location *j*:

```
delivered_price = price + λ × distance(i, j)
```

Distance can be Manhattan distance.

λ is the only spatial control parameter.

---

## Simulation Step

Each time step:

### 1. Production

Each firm produces up to its fixed capacity.

### 2. Demand Allocation

Each grid cell:

* Wants 1 unit of the good
* Chooses the firm with lowest delivered price
* Firm sells if it has remaining capacity

### 3. Revenue

For each firm:

```
money += price × units_sold
```

### 4. Survival Cost

Each firm pays:

```
money -= survival_cost
```

### 5. Death

If:

```
money < 0
```

Firm disappears.

---

## What We Expect

If λ is small:

* Distance barely matters
* Firms compete broadly
* Distribution is more uniform

If λ is large:

* Buyers prefer nearby firms
* Some locations dominate
* Spatial hubs emerge

---

## Metrics to Measure

To test “transport constraints create hubs”:

1. Spatial concentration of output
2. Share of production from top-k firms
3. Size of spatial clusters
4. Average transport distance per unit sold

---

## Important Design Principle

At this stage:

* No productivity bonuses from neighbors
* No collectives
* No extra mechanisms

Only transport cost drives spatial structure.

Later, extensions may include:

* Agglomeration benefits
* Delayed insolvency
* Interdependent goods
* Transport agents

But Stage 1 isolates transport.

---

Sleep well.
Tomorrow we can refine or start implementing cleanly.
