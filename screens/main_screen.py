import os
import logging
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
import matplotlib.pyplot as plt
from models import get_expenses, get_budgets
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

# Configure the logger to flush immediately and capture all levels
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Create a vertical layout
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Create a BoxLayout for graphs
        graph_layout = BoxLayout(orientation='vertical', size_hint_y=0.6)  # 60% of screen height for graphs

        # Add the expense graph
        self.expense_figure, self.expense_ax = plt.subplots(figsize=(6, 4))
        self.expense_canvas = FigureCanvasKivyAgg(self.expense_figure)
        graph_layout.add_widget(self.expense_canvas)

        # Add the budget graph
        self.budget_figure, self.budget_ax = plt.subplots(figsize=(6, 4))
        self.budget_canvas = FigureCanvasKivyAgg(self.budget_figure)
        graph_layout.add_widget(self.budget_canvas)

        layout.add_widget(graph_layout)

        # Create a BoxLayout for the buttons
        button_layout = BoxLayout(size_hint_y=0.2, spacing=dp(10))  # 20% of screen height for buttons

        # Add buttons for navigation
        add_expense_button = MDRaisedButton(text="Add Expense", on_press=self.go_to_add_expense)
        view_reports_button = MDRaisedButton(text="View Reports", on_press=self.go_to_view_reports)
        set_budget_button = MDRaisedButton(text="Set Budget", on_press=self.go_to_set_budget)
        manage_categories_button = MDRaisedButton(text="Manage Categories", on_press=self.go_to_manage_categories)

        button_layout.add_widget(add_expense_button)
        button_layout.add_widget(view_reports_button)
        button_layout.add_widget(set_budget_button)
        button_layout.add_widget(manage_categories_button)

        layout.add_widget(button_layout)

        self.add_widget(layout)

        # Call methods to update graphs
        self.generate_expense_graph()
        self.generate_budget_graph()


    def generate_expense_graph(self):
        try:
            # Fetch expenses from your database
            expenses = get_expenses()

            # Prepare data for the graph
            expense_by_category = {}
            for expense in expenses:
                category = expense[3]
                amount = float(expense[2])
                expense_by_category[category] = expense_by_category.get(category, 0) + amount

            categories = list(expense_by_category.keys())
            amounts = list(expense_by_category.values())

            # Ensure the figure and axis background is transparent
            self.expense_figure.patch.set_alpha(0)  # Transparent figure background
            self.expense_ax.set_facecolor('none')  # Transparent axes background

            # Clear previous chart and plot the pie chart
            self.expense_ax.clear()

            # Determine text color based on the theme
            app = MDApp.get_running_app()
            text_color = "white" if app.theme_cls.theme_style == "Dark" else "black"

            # Plot the pie chart with expense data
            wedges, texts, autotexts = self.expense_ax.pie(amounts, labels=categories, autopct='%1.1f%%')

            # Set the text color for labels and percentages in the pie chart
            for text in texts:
                text.set_color(text_color)
            for autotext in autotexts:
                autotext.set_color(text_color)

            # Redraw the canvas
            self.expense_canvas.draw()

        except Exception as e:
            logging.error(f"Error generating expense graph: {e}")

    def generate_budget_graph(self):
        try:
            # Fetch budgets from your database
            budgets = get_budgets()

            categories = [budget[0] for budget in budgets]
            amounts = [float(budget[1]) for budget in budgets]

            # Clear previous chart and plot the bar chart
            self.budget_ax.clear()

            # Ensure the figure and axis background is transparent
            self.budget_figure.patch.set_alpha(0)  # Transparent figure background
            self.budget_ax.set_facecolor('none')  # Transparent axes background

            # Plot the bar chart
            bars = self.budget_ax.bar(categories, amounts, color=MDApp.get_running_app().theme_cls.primary_color)

            # Set text color based on the theme
            app = MDApp.get_running_app()
            text_color = "white" if app.theme_cls.theme_style == "Dark" else "black"

            # Customize chart labels and text colors
            self.budget_ax.set_xticklabels(categories, color=text_color)
            self.budget_ax.set_yticklabels([0, 50, 100, 150, 200], color=text_color)  # Adjust y-ticks as needed
            self.budget_ax.set_title("Budget Overview", color=text_color)

            # Add data labels on top of bars
            for bar in bars:
                self.budget_ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                                    f'{bar.get_height():.2f}', ha='center', color=text_color)

            # Redraw the canvas
            self.budget_canvas.draw()

        except Exception as e:
            logging.error(f"Error generating budget graph: {e}")

    def load_expenses(self):
        logging.info("Loading all expenses in MainScreen")
        try:
            expenses = get_expenses()
            self.ids.scroll_layout.clear_widgets()

            total = 0
            for expense in expenses:
                amount = float(expense[2])  # Ensure amount is a float
                formatted_amount = f"${amount:,.2f}"  # Format as currency
                expense_label = MDLabel(text=f"{expense[1]}: {formatted_amount} - {expense[3]}", size_hint_y=None, height=40)
                self.ids.scroll_layout.add_widget(expense_label)
                total += amount

            self.ids.total_label.text = f'Total Expenses: ${total:,.2f}'  # Format total as currency
        except Exception as e:
            logging.error(f"Error loading expenses: {e}")

    # Navigation methods
    def go_to_add_expense(self, instance=None):
        self.manager.current = 'add_expense'

    def go_to_view_reports(self, instance=None):
        self.manager.current = 'view_reports'

    def go_to_set_budget(self, instance=None):
        self.manager.current = 'set_budget'

    def go_to_manage_categories(self, instance=None):
        self.manager.current = 'manage_categories'
