from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import logging
from kivy.uix.screenmanager import Screen

class AddExpenseScreen(Screen):
    def __init__(self, **kwargs):
        super(AddExpenseScreen, self).__init__(**kwargs)
        logging.info("AddExpenseScreen initialized")  # Log initialization
        
class AddExpenseScreen(Screen):
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
        self.manager.current = 'main'
