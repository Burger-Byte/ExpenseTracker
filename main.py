
import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from models import add_expense, get_expenses
import logging

logging.basicConfig(level=logging.DEBUG)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        logging.info("Initializing MainScreen")

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Header with total expenses
        self.total_label = Label(text='Total Expenses: $0.00', font_size='20sp', size_hint_y=None, height=50)
        main_layout.add_widget(self.total_label)

        # Scrollable list of recent expenses
        self.scroll_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, 400))
        scroll_view.add_widget(self.scroll_layout)
        main_layout.add_widget(scroll_view)

        # Navigation Buttons
        button_layout = BoxLayout(size_hint_y=None, height=50)
        add_expense_button = Button(text='Add Expense', on_press=self.go_to_add_expense)
        view_reports_button = Button(text='View Reports', on_press=self.go_to_view_reports)
        button_layout.add_widget(add_expense_button)
        button_layout.add_widget(view_reports_button)
        main_layout.add_widget(button_layout)

        self.add_widget(main_layout)

        # Load expenses after the UI is set up
        self.load_expenses()

    def load_expenses(self):
        try:
            expenses = get_expenses()
            logging.info(f"Loaded {len(expenses)} expenses")
            total = 0
            self.scroll_layout.clear_widgets()  # Clear the layout first
            for expense in expenses[:5]:  # Limit to the 5 most recent expenses
                expense_label = Label(text=f"{expense[1]}: ${expense[2]} - {expense[3]}", size_hint_y=None, height=40)
                self.scroll_layout.add_widget(expense_label)
                total += expense[2]

            # Update the total expenses label
            self.total_label.text = f'Total Expenses: ${total:.2f}'

        except Exception as e:
            logging.error(f"Error loading expenses: {e}")

    def go_to_add_expense(self, instance):
        self.manager.current = 'add_expense'

    def go_to_view_reports(self, instance):
        self.manager.current = 'view_reports'

class AddExpenseScreen(Screen):
    def __init__(self, **kwargs):
        super(AddExpenseScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Add Expense Screen'))
        back_button = Button(text='Back to Main Screen')
        back_button.bind(on_press=self.go_back_to_main)
        layout.add_widget(back_button)
        self.add_widget(layout)
    
    def go_back_to_main(self, instance):
        self.manager.current = 'main'

class SimpleApp(App):
    def build(self):
        logging.debug("Building the app")
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddExpenseScreen(name='add_expense'))
        sm.add_widget(AddExpenseScreen(name='view_reports'))
        sm.current = 'main'
        return sm

if __name__ == '__main__':
    try:
        SimpleApp().run()
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}")
