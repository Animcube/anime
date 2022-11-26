from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class happyBirthday(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.gratz = Label(text="Введите имя за чей счет банкет:", font_size=24, color="#FF8C00")
        self.window.add_widget(self.gratz)

        self.inp = TextInput(
            size_hint=(1, 0.2),
            multiline=False,
            padding=10
        )
        self.window.add_widget(self.inp)

        self.but = Button(
            text="ПОЗДРАВИТЬ",
            size_hint=(1, 0.2),
            background_color = "#FF8C00"
        )
        self.but.bind(on_press=self.chng)
        self.window.add_widget(self.but)


        self.window.add_widget(Image(source='resource/aues.png'))

        return self.window

    def chng(self, instance):
        self.gratz.text = "Прими мои глубочайшие поздравления, " + self.inp.text + "!"

if __name__ == '__main__':
    happyBirthday().run()
