import kivy
import os
import logging

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Import your screen classes
from screens.main_screen import MainScreen
from screens.add_expense import AddExpenseScreen
from screens.view_reports import ViewReportsScreen

logging.basicConfig(level=logging.DEBUG)

class ExpenseTrackerApp(App):
    def build(self):
        views_folder = os.path.join(os.path.dirname(__file__), 'views')

        # Load the .kv files separately
        Builder.load_file(os.path.join(views_folder, 'expensetracker.kv'))  # MainScreen
        logging.info("expensetracker.kv loaded")  # Confirm that the file is loaded
        Builder.load_file(os.path.join(views_folder, 'add_expense.kv'))     # AddExpenseScreen
        logging.info("add_expense.kv loaded")  # Confirm that the file is loaded
        Builder.load_file(os.path.join(views_folder, 'view_reports.kv'))    # ViewReportsScreen, if needed
        logging.info("view_reports.kv loaded")  # Confirm that the file is loaded

        # Set up ScreenManager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddExpenseScreen(name='add_expense'))
        logging.info("AddExpenseScreen added to ScreenManager")
        sm.add_widget(ViewReportsScreen(name='view_reports'))  # Ensure other screens are added
        logging.info("ViewReprotsScreen added to ScreenManager")

        return sm

if __name__ == '__main__':
    try:
        ExpenseTrackerApp().run()
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}")
