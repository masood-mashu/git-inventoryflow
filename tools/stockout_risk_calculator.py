"""
stockout_risk_calculator.py - Calculates days of supply remaining based on current on-hand stock and daily velocity
"""
import sys
import json


def calculate_stockout_risk(sku_data_json: str, min_days_threshold: int = 7):
    import json
    data = json.loads(sku_data_json) if isinstance(sku_data_json, str) else sku_data_json
    on_hand = data.get("on_hand", 0)
    velocity = max(data.get("daily_sales_velocity", 1.0), 0.1)
    days_left = on_hand / velocity
    is_risk = days_left < min_days_threshold
    return {
        "on_hand": on_hand,
        "daily_velocity": velocity,
        "days_of_supply": round(days_left, 1),
        "stockout_risk": is_risk,
        "status": "CRITICAL_STOCKOUT_RISK" if is_risk else "HEALTHY_STOCK"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "stockout-risk-calculator"}))
