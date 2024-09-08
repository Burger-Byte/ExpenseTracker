# add_expense.py
from screens.base_screen import BaseScreen

class AddExpenseScreen(BaseScreen):
    def save_expense(self):
        data = {
            'amount': self.ids.amount_input.text,
            'category': self.ids.category_input.text,
            'description': self.ids.description_input.text,
            'date': self.ids.date_label.text
        }
        self.save_data('expense', data)

    def go_back_to_main(self):
        self.go_to_screen('main')
