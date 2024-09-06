import os
import logging
from screens.main_screen import MainScreen


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
from kivy.uix.boxlayout import BoxLayout

logging.debug("Starting the ExpenseTracker app")

class ExpenseTrackerApp(MDApp):
    def build(self):
        try:
            self.theme_cls.primary_palette = "Blue"
            self.theme_cls.theme_style = "Dark"
            logging.debug("Theme set to Blue and Dark")

            # Set up the database and default categories
            setup_database()
            setup_default_categories()
            logging.debug("Database and default categories set up")

            # Load .kv files
            views_folder = os.path.join(os.path.dirname(__file__), 'views')

            kv_files = ['main_screen.kv', 'add_expense.kv', 'view_reports.kv', 'budget.kv', 'manage_categories.kv']
            for kv_file in kv_files:
                kv_path = os.path.join(views_folder, kv_file)
                if os.path.exists(kv_path):
                    Builder.load_file(kv_path)
                    logging.debug(f"{kv_file} loaded")
                else:
                    logging.error(f"{kv_file} not found in {views_folder}")

            # Initialize ScreenManager
            sm = ScreenManager()
            sm.add_widget(MainScreen(name='main'))
            sm.add_widget(AddExpenseScreen(name='add_expense'))
            sm.add_widget(ViewReportsScreen(name='view_reports'))
            sm.add_widget(SetBudgetScreen(name='set_budget'))
            sm.add_widget(ManageCategoriesScreen(name='manage_categories'))
            logging.debug("All screens added to ScreenManager")

            return sm
        except Exception as e:
            logging.critical(f"Unhandled exception: {e}")
            raise e

if __name__ == '__main__':
    ExpenseTrackerApp().run()