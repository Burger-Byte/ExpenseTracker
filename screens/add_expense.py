from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
import logging
from models import add_expense
from datetime import datetime

class AddExpenseScreen(MDScreen):
    selected_date = None  # Variable to store the selected date

    def show_date_picker(self):
        # Create a date picker instance
        date_picker = MDDatePicker()
        # Bind the on_save event to handle the selected date
        date_picker.bind(on_save=self.on_date_selected)
        date_picker.open()

    def on_date_selected(self, instance, value, date_range):
        # Store the selected date and display it
        self.selected_date = value
        self.ids.date_label.text = f"Selected Date: {value.strftime('%Y-%m-%d')}"
        logging.info(f"Date selected: {value}")

    def save_expense(self):
        # Ensure a date is selected
        if self.selected_date:
            date = self.selected_date.strftime('%Y-%m-%d')  # Convert to string in YYYY-MM-DD format
        else:
            logging.error("No date selected")
            return  # Don't save without a date

        amount = self.ids.amount_input.text
        category = self.ids.category_input.text
        description = self.ids.description_input.text

        # Validate the amount as a float
        try:
            amount = float(amount)
        except ValueError:
            logging.error("Invalid amount entered")
            return

        # Save the data using your add_expense function from models.py
        add_expense(date, amount, category, description)

        # Clear the input fields after saving
        self.ids.amount_input.text = ""
        self.ids.category_input.text = ""
        self.ids.description_input.text = ""
        self.selected_date = None
        self.ids.date_label.text = "Selected Date: None"
        logging.info(f"Expense saved with date: {date}, amount: {amount}, category: {category}, description: {description}")

    def go_back_to_main(self):
        logging.info("Navigating back to MainScreen")
        self.manager.current = 'main'

        # Use a Clock to schedule the loading of expenses to ensure the UI has time to switch screens
        from kivy.clock import Clock
        Clock.schedule_once(self.refresh_main_screen, 0.1)

    def refresh_main_screen(self, *args):
        main_screen = self.manager.get_screen('main')
        logging.info("Refreshing MainScreen and loading expenses")
        main_screen.load_expenses()
