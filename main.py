from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'borderless', 0)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 720)

class CustomBoxLayout(BoxLayout):
    pass

class Dashboard(App):
    def build(self):
        root = CustomBoxLayout()
        return root

Dashboard().run()