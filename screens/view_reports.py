from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import logging
from kivy.uix.screenmanager import Screen

class ViewReportsScreen(Screen):
    def __init__(self, **kwargs):
        logging.info("ViewReportsScreen initialized")  # Log initialization
        super(ViewReportsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='View Reports Screen'))
        back_button = Button(text='Back to Main Screen')
        back_button.bind(on_press=self.go_back_to_main)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back_to_main(self, instance):
        self.manager.current = 'main'
