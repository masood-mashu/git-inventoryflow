"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitInventoryFlow.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.stockout_risk_calculator import *
from tools.reorder_point_evaluator import *
from tools.dead_stock_detector import *

class TestGitInventoryFlowPredictability(unittest.TestCase):

    def test_stockout_risk_calculator(self):
        res = calculate_stockout_risk('{"on_hand": 20, "daily_sales_velocity": 5.0}')
        self.assertTrue(res["stockout_risk"])
        self.assertEqual(res["status"], "CRITICAL_STOCKOUT_RISK")

    def test_reorder_point_evaluator(self):
        res = evaluate_reorder_point('{"daily_demand": 10, "lead_time_days": 5, "safety_stock": 25}')
        self.assertEqual(res["reorder_point"], 75)
        self.assertEqual(res["status"], "REORDER_POINT_CALCULATED")

    def test_dead_stock_detector(self):
        res = detect_dead_stock(75, dead_stock_threshold=60)
        self.assertTrue(res["is_dead_stock"])
        self.assertEqual(res["status"], "DEAD_STOCK_FLAG")


if __name__ == "__main__":
    unittest.main()
