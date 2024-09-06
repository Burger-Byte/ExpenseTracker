import os
import logging

# Set up logging at the entry point of the application
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

# Now proceed with the rest of your imports and app setup
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.main_screen import MainScreen
from screens.add_expense import AddExpenseScreen
from screens.view_reports import ViewReportsScreen
from screens.budget import SetBudgetScreen
from models import setup_database, setup_default_categories
from screens.manage_categories import ManageCategoriesScreen

class ExpenseTrackerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"  # Set primary color
        self.theme_cls.theme_style = "Dark"  # Choose between 'Light' and 'Dark'
        
        # Set up the database and default categories
        setup_database()
        setup_default_categories()  # Ensure default categories are set up

        # Load .kv files and screens
        views_folder = os.path.join(os.path.dirname(__file__), 'views')

        Builder.load_file(os.path.join(views_folder, 'main_screen.kv'))
        Builder.load_file(os.path.join(views_folder, 'add_expense.kv'))
        Builder.load_file(os.path.join(views_folder, 'view_reports.kv'))
        Builder.load_file(os.path.join(views_folder, 'budget.kv'))
        Builder.load_file(os.path.join(views_folder, 'manage_categories.kv'))

        # Initialize ScreenManager and screens
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddExpenseScreen(name='add_expense'))
        sm.add_widget(ViewReportsScreen(name='view_reports'))
        sm.add_widget(SetBudgetScreen(name='set_budget'))
        sm.add_widget(ManageCategoriesScreen(name='manage_categories'))

        return sm

if __name__ == '__main__':
    ExpenseTrackerApp().run()
