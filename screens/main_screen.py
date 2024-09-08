import os
import logging
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
from screens.base_screen import BaseScreen
from models import get_expenses, get_budgets
from kivymd.app import MDApp


class MainScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.graphs_dir = os.path.join(os.getcwd(), 'graphs')
        if not os.path.exists(self.graphs_dir):
            os.makedirs(self.graphs_dir)

        self.setup_graphs()

    def setup_graphs(self):
        """Set up the graphs (expense and budget) using matplotlib with transparency and dynamic colors."""
        graph_layout = self.ids.graph_layout

        # Expense graph setup
        self.expense_figure, self.expense_ax = plt.subplots(figsize=(6, 4))
        self.expense_canvas = FigureCanvasKivyAgg(self.expense_figure)
        graph_layout.add_widget(self.expense_canvas)

        # Budget graph setup
        self.budget_figure, self.budget_ax = plt.subplots(figsize=(6, 4))
        self.budget_canvas = FigureCanvasKivyAgg(self.budget_figure)
        graph_layout.add_widget(self.budget_canvas)

        # Generate the graphs
        self.generate_expense_graph()
        self.generate_budget_graph()

    def generate_expense_graph(self):
        """Generate a pie chart for expenses with dynamic color and transparent background."""
        expenses = get_expenses()
        category_totals = {}

        # Aggregate expenses by category
        for expense in expenses:
            category = expense[3]
            amount = float(expense[2])
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        # Clear the previous graph
        self.expense_ax.clear()

        # Set figure and axes to be transparent
        self.expense_figure.patch.set_alpha(0)  # Make figure background transparent
        self.expense_ax.set_facecolor('none')   # Make axis background transparent

        # Determine if the theme is light or dark
        app = MDApp.get_running_app()
        text_color = "white" if app.theme_cls.theme_style == "Dark" else "black"

        # Create the pie chart
        self.expense_ax.pie(amounts, labels=categories, autopct='%1.1f%%', textprops={'color': text_color})
        self.expense_canvas.draw()

    def generate_budget_graph(self):
        """Generate a stacked bar chart comparing budgets and expenses with dynamic colors."""
        budgets = get_budgets()
        expenses = get_expenses()

        # Aggregate expenses by category
        expense_by_category = {}
        for expense in expenses:
            category = expense[3]
            amount = float(expense[2])
            if category in expense_by_category:
                expense_by_category[category] += amount
            else:
                expense_by_category[category] = amount

        categories = [budget[0] for budget in budgets]
        budget_amounts = [float(budget[1]) for budget in budgets]
        expense_amounts = [expense_by_category.get(category, 0) for category in categories]

        # Clear the previous graph
        self.budget_ax.clear()

        # Set figure and axes to be transparent
        self.budget_figure.patch.set_alpha(0)
        self.budget_ax.set_facecolor('none')

        # Determine if the theme is light or dark
        app = MDApp.get_running_app()
        text_color = "white" if app.theme_cls.theme_style == "Dark" else "black"

        # Plot the budget and expenses as stacked bars
        bar_width = 0.5
        budget_bars = self.budget_ax.bar(categories, budget_amounts, bar_width, label='Budget',
                                         color=app.theme_cls.primary_color)
        expense_bars = self.budget_ax.bar(categories, expense_amounts, bar_width, label='Expenses',
                                          color='red', alpha=0.7)

        # Customize chart labels and text colors
        self.budget_ax.set_xticklabels(categories, color=text_color, rotation=45, ha='right')
        self.budget_ax.set_yticklabels([0, 100, 200, 300, 400, 500], color=text_color)
        self.budget_ax.set_title("Expenses Overview", color=text_color)

        # Add labels on top of each bar for expenses and budget
        for i, (budget_bar, expense_bar) in enumerate(zip(budget_bars, expense_bars)):
            self.budget_ax.text(budget_bar.get_x() + budget_bar.get_width() / 2,
                                budget_bar.get_height(), f'{budget_amounts[i]:.2f}', ha='center', color=text_color)
            self.budget_ax.text(expense_bar.get_x() + expense_bar.get_width() / 2,
                                expense_bar.get_height(), f'{expense_amounts[i]:.2f}', ha='center', color=text_color)

        # Add legend
        self.budget_ax.legend()

        self.budget_canvas.draw()

    def on_pre_enter(self):
        """Refresh graphs before entering the screen."""
        self.generate_expense_graph()
        self.generate_budget_graph()
