# GitInventoryFlow Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitInventoryFlow** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitInventoryFlow consumes warehouse inventory balances, point-of-sale checkout telemetry, supplier replenishment schedules, and omnichannel fulfillment manifests. These data sources include SKU identifiers, on-hand physical stock counts, rolling 14-day sales velocity numbers, and supplier lead-time parameters. The agent ingests these inputs in raw JSON, CSV, and EDI transaction format and parses them into standardized supply chain planning models for downstream analysis. Regional distribution center capacity tables and seasonal promotion schedules are also monitored as sensitive data sources to ensure product availability is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an inventory snapshot is processed, the agent first evaluates supply continuity using the stockout-risk-calculator tool to identify SKUs with less than 7 days of supply remaining. Next, the reasoning engine invokes the reorder-point-evaluator tool to compute optimal replenishment triggers accounting for vendor lead time and safety stock buffers. Furthermore, stagnant items are evaluated using the dead-stock-detector tool to identify liquidation opportunities. Finally, the agent correlates all inventory metrics against predefined retail policies to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated purchase requisition.

---

## 3. Constraints, Limitations, and Known Issues

GitInventoryFlow operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitInventoryFlow operates under strict operational constraints to prevent costly stockouts and excessive capital lockup across retail supply chains. The agent is deliberately limited to mathematical demand modeling and reorder calculations and cannot independently resolve physical warehouse discrepancies caused by shrinkage or damage. Another known issue and limitation is that sudden external viral demand shocks without preceding signals may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
