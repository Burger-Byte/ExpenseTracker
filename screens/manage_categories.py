# manage_categories.py
from screens.base_screen import BaseScreen

class ManageCategoriesScreen(BaseScreen):
    def add_category(self):
        category_name = self.ids.category_input.text
        self.save_data('category', {'name': category_name})

    def go_back_to_main(self):
        self.go_to_screen('main')
