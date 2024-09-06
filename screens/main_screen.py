from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from models import get_expenses
from kivymd.uix.label import MDLabel
import logging
import sys

# Configure the logger to flush immediately and capture all levels
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        logging.info("MainScreen initialized")  # This should only be printed once

    def on_pre_enter(self):
        logging.info("MainScreen is about to be displayed")
        self.load_expenses()  # Uncomment this to load expenses when navigating back to the MainScreen

    def load_expenses(self):
        logging.info("Loading all expenses in MainScreen")
        try:
            expenses = get_expenses()
            logging.info(f"Loaded {len(expenses)} expenses")

            self.ids.scroll_layout.clear_widgets()

            total = 0
            for expense in expenses:
                amount = float(expense[2])  # Ensure amount is a float
                formatted_amount = f"${amount:,.2f}"  # Format as currency

                # Display the expense
                expense_label = MDLabel(text=f"{expense[1]}: {formatted_amount} - {expense[3]}", size_hint_y=None, height=40)
                self.ids.scroll_layout.add_widget(expense_label)

                total += amount

            self.ids.total_label.text = f'Total Expenses: ${total:,.2f}'  # Format total as currency

        except Exception as e:
            logging.error(f"Error loading expenses: {e}")

    def go_to_add_expense(self):
        logging.info("Navigating to Add Expenses Screen")
        self.manager.current = 'add_expense'

    def go_to_view_reports(self):
        logging.info("Navigating to View Reports Screen")
        self.manager.current = 'view_reports'
    
    def go_to_set_budget(self):
        logging.info("Navigating to Set Budget Screen")
        self.manager.current = 'set_budget'

    def go_to_manage_categories(self):
        logging.info("Navigating to Manage Categories Screen")
        self.manager.current = 'manage_categories'
