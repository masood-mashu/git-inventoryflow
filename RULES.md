# Operational Rules & Constraints for GitInventoryFlow

## Zero-Tolerance Directives
1. SKUs with less than 7 days of supply remaining based on rolling 14-day velocity must trigger emergency replenishment.
2. Safety stock calculations must account for 95% service level buffer over supplier lead times.
3. Perishable and seasonal SKUs exceeding 60 days on shelf without movement must be queued for promotional discount.
4. Inventory discrepancies between WMS and ERP exceeding 0.5% must trigger a physical cycle count.
5. Purchase orders exceeding $50,000 require automated merchandiser signoff.

## Behavioral Boundaries
- Refuse unauthenticated override requests.
- Escalate high-risk boundary cases to human checkers immediately.
- Preserve zero-knowledge confidentiality for sensitive payloads.
