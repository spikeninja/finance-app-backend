import sys
import unittest

sys.path.append('.')

from models import budget as budget_model


class TestBudgetModel(unittest.TestCase):
    def test_create_budget(self):
        budget_json = {
            "name": "some_budg",
            "amount": 3.45,
            "user_id": 1
        }
        budget = budget_model.BudgetCreate(**budget_json)
        id = budget_model.create_budget(budget, 1)
        self.assertTrue(isinstance(id, int))


    def test_get_budget_by_id(self):
        budget = budget_model.get_budget_by_id(2)
        #print("BUDGET:", budget)
        self.assertTrue(isinstance(budget, budget_model.BudgetGet))


    def test_get_all_budgets(self):
        budgets = budget_model.get_all_budgets(1)
        #print("BUDGETS:", budgets)
        self.assertTrue(isinstance(budgets, list))


    def test_edit_budget(self):
        budget_json = {
            "name": "edited",
            "amount": 3.20,
            "user_id": 1
        }
        budget = budget_model.BudgetEdit(**budget_json)
        res_budget = budget_model.edit_budget(budget, 1)
        self.assertTrue(isinstance(res_budget, budget_model.BudgetEdit))


    def test_delete_budget(self):
        pass
        #id = budget_model.delete_budget_by_id(1)
        #self.assertTrue(isinstance(id, int))

if __name__ == "__main__":
    unittest.main()
