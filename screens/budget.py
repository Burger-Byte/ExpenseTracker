# budget.py
from screens.base_screen import BaseScreen

class SetBudgetScreen(BaseScreen):
    def save_budget(self):
        data = {
            'category': self.ids.category_input.text,
            'budget': self.ids.budget_input.text
        }
        self.save_data('budget', data)

    def go_back_to_main(self):
        self.go_to_screen('main')
