# base_screen.py

import logging
from kivy.uix.screenmanager import Screen

class BaseScreen(Screen):
    def go_to_screen(self, screen_name):
        logging.info(f"Navigating to {screen_name} Screen")
        self.manager.current = screen_name

    def save_data(self, data_type, data):
        logging.info(f"Saving {data_type}: {data}")
        # Logic for saving data based on the type
        # Placeholder for actual save logic (can be connected to models)
        if data_type == 'expense':
            # Save expense logic
            pass
        elif data_type == 'budget':
            # Save budget logic
            pass
        elif data_type == 'category':
            # Save category logic
            pass

    def generate_graph(self, ax, data, labels, graph_type='pie'):
        ax.clear()
        if graph_type == 'pie':
            ax.pie(data, labels=labels, autopct='%1.1f%%')
        elif graph_type == 'bar':
            ax.bar(labels, data)
        ax.figure.canvas.draw()
