# main.py
import os
import logging
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from screens.main_screen import MainScreen
from screens.add_expense import AddExpenseScreen
from screens.view_reports import ViewReportsScreen
from screens.budget import SetBudgetScreen
from screens.manage_categories import ManageCategoriesScreen
from models import setup_database, setup_default_categories

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
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

            # Initialize ScreenManager and add screens
            self.screen_manager = ScreenManager()
            self.screen_manager.add_widget(MainScreen(name='main'))
            self.screen_manager.add_widget(AddExpenseScreen(name='add_expense'))
            self.screen_manager.add_widget(ViewReportsScreen(name='view_reports'))
            self.screen_manager.add_widget(SetBudgetScreen(name='set_budget'))
            self.screen_manager.add_widget(ManageCategoriesScreen(name='manage_categories'))
            logging.debug("All screens added to ScreenManager")

            # Create bottom navigation
            bottom_nav = MDBottomNavigation()

            # Tab for Main Screen
            bottom_nav_item_main = MDBottomNavigationItem(
                name="main",
                text="Main",
                icon="home",
                on_tab_press=lambda _: self.switch_screen('main')
            )
            bottom_nav.add_widget(bottom_nav_item_main)

            # Tab for Add Expense
            bottom_nav_item_expense = MDBottomNavigationItem(
                name="add_expense",
                text="Add Expense",
                icon="plus-box",
                on_tab_press=lambda _: self.switch_screen('add_expense')
            )
            bottom_nav.add_widget(bottom_nav_item_expense)

            # Tab for View Reports
            bottom_nav_item_reports = MDBottomNavigationItem(
                name="view_reports",
                text="Reports",
                icon="chart-bar",
                on_tab_press=lambda _: self.switch_screen('view_reports')
            )
            bottom_nav.add_widget(bottom_nav_item_reports)

            # Tab for Set Budget
            bottom_nav_item_budget = MDBottomNavigationItem(
                name="set_budget",
                text="Budget",
                icon="currency-usd",
                on_tab_press=lambda _: self.switch_screen('set_budget')
            )
            bottom_nav.add_widget(bottom_nav_item_budget)

            # Tab for Manage Categories
            bottom_nav_item_categories = MDBottomNavigationItem(
                name="manage_categories",
                text="Categories",
                icon="format-list-bulleted",
                on_tab_press=lambda _: self.switch_screen('manage_categories')
            )
            bottom_nav.add_widget(bottom_nav_item_categories)

            # Create a BoxLayout to hold both the ScreenManager and the BottomNavigation
            root_layout = BoxLayout(orientation='vertical')
            root_layout.add_widget(self.screen_manager)
            root_layout.add_widget(bottom_nav)

            return root_layout

        except Exception as e:
            logging.critical(f"Unhandled exception: {e}")
            raise e

    def switch_screen(self, screen_name):
        """Switch to a screen by name."""
        try:
            self.screen_manager.current = screen_name
            logging.debug(f"Switched to {screen_name} screen")
        except Exception as e:
            logging.error(f"Error switching to screen {screen_name}: {e}")
            raise e


if __name__ == '__main__':
    ExpenseTrackerApp().run()
