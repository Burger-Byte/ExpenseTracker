from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
import logging
from models import get_categories, add_category, delete_category

class ManageCategoriesScreen(MDScreen):
    def on_enter(self):
        self.load_categories()

    def load_categories(self):
        logging.info("Loading categories in ManageCategoriesScreen")
        categories = get_categories()

        self.ids.categories_list.clear_widgets()
        for category in categories:
            category_button = MDRaisedButton(text=category, on_press=lambda x: self.delete_category(category))
            self.ids.categories_list.add_widget(category_button)

    def add_category(self):
        new_category = self.ids.category_input.text
        if new_category:
            add_category(new_category)
            self.ids.category_input.text = ""  # Clear input
            self.load_categories()  # Reload categories
        else:
            logging.warning("Category name cannot be empty")

    def delete_category(self, category_name):
        delete_category(category_name)
        self.load_categories()  # Reload categories after deletion

    def go_back_to_main(self):
        logging.info("Navigating back to MainScreen")
        self.manager.current = 'main'
