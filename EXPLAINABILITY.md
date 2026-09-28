# Explainability & Governance Statement

## Decision Architecture
GitInventoryFlow evaluates inventory health using classical supply chain equations. By dividing on-hand stock by average daily sales, the agent computes days-of-supply. If the remaining inventory drops below lead time plus safety buffer, the agent triggers an immediate reorder recommendation with exact economic order quantities (EOQ).

## Input Data Provenance
Data sources include warehouse management system (WMS) inventory snapshots, ERP purchase order catalogs, and multi-channel checkout feeds.

## Operational Limits & Non-Goals
GitInventoryFlow relies on reported physical stock counts; it cannot independently prevent physical theft (shrinkage) or warehouse water damage.
