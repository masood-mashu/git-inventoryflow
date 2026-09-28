# Separation of Duties for GitInventoryFlow

## Maker Role: InventoryPlanner
InventoryPlanner who models SKU demand forecasts, replenishment schedules, and safety buffers.

## Checker Role: MerchandisingDirector
MerchandisingDirector who approves procurement runs, stock transfers, and markdown actions.

## Dual-Control Verification Pipeline
1. Ingest point-of-sale (POS) and e-commerce channel transactional velocities.
2. Calculate SKU-level days-of-supply based on current on-hand quantities.
3. Evaluate optimal reorder points factoring in vendor transit lead time.
4. Produce replenishment purchase requisitions and stock reallocation orders.
