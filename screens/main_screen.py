from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from models import get_expenses
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
        logging.info("Loading expenses in MainScreen")
        try:
            expenses = get_expenses()
            logging.info(f"Loaded {len(expenses)} expenses")
            total = 0
            
            # Access scroll_layout from kv file using self.ids
            self.ids.scroll_layout.clear_widgets()  # Clear the layout first
            
            for expense in expenses[:5]:
                expense_label = Label(text=f"{expense[1]}: ${expense[2]} - {expense[3]}", size_hint_y=None, height=40)
                self.ids.scroll_layout.add_widget(expense_label)
                total += expense[2]
    
            # Update the total expenses label
            self.ids.total_label.text = f'Total Expenses: ${total:.2f}'
    
            self.ids.total_label.texture_update()
            self.ids.scroll_layout.do_layout()
    
        except Exception as e:
            logging.error(f"Error loading expenses: {e}")

    def go_to_add_expense(self):
        logging.info("Navigating to Add Expenses Screen")
        self.manager.current = 'add_expense'

    def go_to_view_reports(self):
        logging.info("Navigating to View Reports Screen")
        self.manager.current = 'view_reports'
