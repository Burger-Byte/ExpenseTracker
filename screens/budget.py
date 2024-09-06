from kivymd.uix.screen import MDScreen
import logging
from models import set_budget

class SetBudgetScreen(MDScreen):
    def save_budget(self):
        category = self.ids.category_input.text
        budget = self.ids.budget_input.text

        # Ensure both category and budget are provided
        if category and budget:
            try:
                budget_amount = float(budget)  # Convert budget to float
                set_budget(category, budget_amount)  # Save the budget to the database
                logging.info(f"Budget set: {category} with amount {budget_amount}")
                
                # Clear the input fields
                self.ids.category_input.text = ""
                self.ids.budget_input.text = ""

            except ValueError:
                logging.error("Invalid budget amount. Please enter a valid number.")
        else:
            logging.error("Both category and budget amount are required.")

    def go_back_to_main(self):
        logging.info("Navigating back to MainScreen")
        self.manager.current = 'main'
