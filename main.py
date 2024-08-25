# main.py

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from models import add_expense

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        btn = Button(text='Go to Add Expense Screen')
        btn.bind(on_press=self.switch_to_add_expense)
        self.add_widget(btn)
    
    def switch_to_add_expense(self, *args):
        self.manager.current = 'add_expense'

class AddExpenseScreen(Screen):
    def __init__(self, **kwargs):
        super(AddExpenseScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        self.date_input = TextInput(hint_text='Date (YYYY-MM-DD)')
        self.amount_input = TextInput(hint_text='Amount')
        self.category_input = TextInput(hint_text='Category')
        self.description_input = TextInput(hint_text='Description')
        
        layout.add_widget(self.date_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.category_input)
        layout.add_widget(self.description_input)
        
        btn = Button(text='Save Expense')
        btn.bind(on_press=self.save_expense)
        layout.add_widget(btn)
        
        back_btn = Button(text='Back to Main Screen')
        back_btn.bind(on_press=self.switch_to_main)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def save_expense(self, *args):
        # Save the data to the database
        add_expense(self.date_input.text, self.amount_input.text, self.category_input.text, self.description_input.text)
        print("Expense saved!")
        self.manager.current = 'main'

    def switch_to_main(self, *args):
        self.manager.current = 'main'

class SimpleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddExpenseScreen(name='add_expense'))
        sm.current = 'main'
        return sm

if __name__ == '__main__':
    SimpleApp().run()
