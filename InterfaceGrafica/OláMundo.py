#coding=utf-8
from kivy.app import App
from kivy.uix.button import Button

class Tela(App):
    def build(self):
        return Button(text='Olá, Mundo!', font_size=50)

Tela().run()