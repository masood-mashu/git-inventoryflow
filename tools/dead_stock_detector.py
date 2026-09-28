"""
dead_stock_detector.py - Identifies dormant inventory SKUs with zero units sold over a specified observation window
"""
import sys
import json


def detect_dead_stock(days_without_sale: int, dead_stock_threshold: int = 60):
    is_dead = days_without_sale >= dead_stock_threshold
    return {
        "days_inactive": days_without_sale,
        "threshold": dead_stock_threshold,
        "is_dead_stock": is_dead,
        "recommended_action": "PROMOTIONAL_MARKDOWN" if is_dead else "MAINTAIN_PRICING",
        "status": "DEAD_STOCK_FLAG" if is_dead else "ACTIVE_INVENTORY"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "dead-stock-detector"}))
