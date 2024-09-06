from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp
import logging
from models import get_expense_reports

class ViewReportsScreen(MDScreen):
    def on_enter(self):
        # This is called when the screen is shown
        self.load_reports()

    def load_reports(self):
        logging.info("Loading reports in ViewReportsScreen")
        
        # Clear previous reports
        self.ids.reports_list.clear_widgets()

        # Retrieve report data from the model
        reports = get_expense_reports()

        for report in reports:
            # Create a card for each report
            card = MDCard(orientation='vertical', padding=dp(10), size_hint=(1, None), height=dp(100))
            card.add_widget(MDLabel(text=f"Category: {report['category']}", font_style="H6"))
            card.add_widget(MDLabel(text=f"Total Spent: ${report['total']:.2f}"))

            # Add the card to the layout
            self.ids.reports_list.add_widget(card)

    def go_back_to_main(self):
        logging.info("Navigating back to MainScreen")
        self.manager.current = 'main'
