import logging
from kivy.uix.screenmanager import Screen
from models import add_expense

class AddExpenseScreen(Screen):
    def __init__(self, **kwargs):
        super(AddExpenseScreen, self).__init__(**kwargs)
        logging.info("AddExpenseScreen initialized")  # Log initialization

    def save_expense(self):
        # Get the data from the inputs
        date = self.ids.date_input.text
        amount = self.ids.amount_input.text
        category = self.ids.category_input.text
        description = self.ids.description_input.text

        # Save the data (using your add_expense function from models.py)
        add_expense(date, amount, category, description)

        # Clear the input fields after saving
        self.ids.date_input.text = ""
        self.ids.amount_input.text = ""
        self.ids.category_input.text = ""
        self.ids.description_input.text = ""

    def go_back_to_main(self):
        logging.info("Navigating back to MainScreen")
        self.manager.current = 'main'
        
        # Force the main screen to refresh after adding an expense
        main_screen = self.manager.get_screen('main')
        logging.info("Forcing MainScreen to load expenses")
        # Temporarily comment this to test if it’s causing the recursion
        main_screen.load_expenses()