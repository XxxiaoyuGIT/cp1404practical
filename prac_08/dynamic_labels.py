from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        # Data (list of names)
        names = ["Kana", "Kokomi", "Lisana", "Ellis"]

        # Root widget
        root = BoxLayout(orientation='vertical')

        # Create Labels dynamically
        for name in names:
            label = Label(text=name)
            root.add_widget(label)

        return root

if __name__ == '__main__':
    SimpleApp().run()
