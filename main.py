import os
import logging

# Set up logging at the entry point of the application
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

# Now proceed with the rest of your imports and app setup
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.main_screen import MainScreen
from screens.add_expense import AddExpenseScreen
from screens.view_reports import ViewReportsScreen

class ExpenseTrackerApp(App):
    def build(self):
        # Load .kv files and screens
        views_folder = os.path.join(os.path.dirname(__file__), 'views')
        Builder.load_file(os.path.join(views_folder, 'expensetracker.kv'))
        Builder.load_file(os.path.join(views_folder, 'add_expense.kv'))
        Builder.load_file(os.path.join(views_folder, 'view_reports.kv'))

        # Initialize ScreenManager and screens
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddExpenseScreen(name='add_expense'))
        sm.add_widget(ViewReportsScreen(name='view_reports'))

        return sm

if __name__ == '__main__':
    ExpenseTrackerApp().run()
