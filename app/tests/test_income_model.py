import unittest
import sys

sys.path.append('.')

from models import income as income_model


class TestIncomeModel(unittest.TestCase):
    def test_create_income(self):
        income_json = {
            "description":"some_description",
            "amount":3.25,
            "category":"you know"
        }
        income = income_model.IncomeCreate(
            **income_json
        )
        income_id = income_model.create_income(income, 2)
        self.assertTrue(isinstance(income_id,
                        income_model.IncomeCreate))


    #def test_get_income_by_id(self):
        #income = income_model.get_income_by_id(4)
        #self.assertTrue(isinstance(income,
                        #income_model.IncomeGet))


    def test_get_all_incomes(self):
        incomes = income_model.get_all_incomes(2)
        self.assertTrue(isinstance(incomes, list))


    def test_get_income_in_period(self):
        pass


    def test_edit_income(self):
        income_json = {
            "description":"edited_description",
            "amount":6.23,
            "category":"I know"
        }
        income = income_model.IncomeCreate(
            **income_json
        )
        income = income_model.edit_income(income, 1)
        self.assertTrue(isinstance(income,
                        income_model.IncomeCreate))


    def test_delete_income(self):
        income_id = income_model.delete_income(1)
        self.assertTrue(isinstance(income_id, int))


if __name__ == "__main__":
    unittest.main()
