# Segregation of Duties (SOD) Policy: GitInventoryFlow

This document establishes the role boundaries and segregation of duties for the GitInventoryFlow agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring inventory replenishment orders, adjusting demand forecasts, and preparing automated supply diffs.
This role cannot approve or merge its own changes into protected ERP procurement branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming purchase orders, stockout alerts, and reorder point calculations.
This role operates as an impartial auditor to verify compliance with enterprise merchandising benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Inventory Directors and Chief Supply Chain Officers.
Human approval is required for all high-value procurement executions and safety stock policy overrides.
