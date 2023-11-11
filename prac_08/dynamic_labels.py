from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

Names = ["Kana", "Lisana", "Kokomi", "Xiao", "Furina"]


class DynamicLabels(App):
    """"""
    status_text = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = Names
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root
    def create_widgets(self):
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)


DynamicLabels().run()