"""
reorder_point_evaluator.py - Calculates optimal reorder point accounting for supplier lead time and safety stock buffer
"""
import sys
import json


def evaluate_reorder_point(reorder_data_json: str):
    import json
    data = json.loads(reorder_data_json) if isinstance(reorder_data_json, str) else reorder_data_json
    demand = data.get("daily_demand", 20)
    lead_time = data.get("lead_time_days", 10)
    safety = data.get("safety_stock", 50)
    rop = (demand * lead_time) + safety
    return {
        "daily_demand": demand,
        "lead_time_days": lead_time,
        "safety_stock": safety,
        "reorder_point": rop,
        "status": "REORDER_POINT_CALCULATED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "reorder-point-evaluator"}))
