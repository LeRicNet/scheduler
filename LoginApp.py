import kivy
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

class Login(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    super().__init__()
    return 0

class LoginApp(App):

    def build(self):
        return Login(info='Hello world')


if __name__ == '__main__':
    LoginApp().run()