import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


kivy.require('2.3.0')

class CalculatorApp(App):

    def build(self):
        layout = GridLayout(cols=4)

        self.result = TextInput(multiline=False, readonly = True, font_size = 10)
        layout.add_widget(self.result)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for label in buttons:
            button = Button(text=label, font_size=40)
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)

        return layout
    

    def on_button_press(self,instance):
        if instance.text == "=":
            try:
                self.result.text = str(eval(self.result.text))
            except:
                self.result.text = 'Error'
        elif instance.text == "C":
            self.result.text = ''
        else:
            self.result.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()
    
