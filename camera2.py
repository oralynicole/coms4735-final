from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
import os
import time
import cv2


# Process
from process import process

class CameraScreen(Screen):

    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.camera = Camera(resolution=(640, 480), play=True)
        button = Button(text='Take Picture')
        button.size_hint = (0.2, 0.2)
        button.pos_hint = {'x': 0.4, 'y': 0}
        button.bind(on_press=self.take_picture)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.camera)
        layout.add_widget(button)
        self.add_widget(layout)

    def take_picture(self, event):
        timestamp = str(time.time())
        img = self.camera.texture
        filename = "./book.png"
        img.save(filename)
        App.get_running_app().image_filename = filename
        App.get_running_app().sm.current = 'preview'

class PreviewScreen(Screen):

    def __init__(self, **kwargs):
        super(PreviewScreen, self).__init__(**kwargs)
        self.image = Image()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.image)
        button = Button(text='Process Image')
        button.size_hint = (0.2, 0.2)
        button.pos_hint = {'x': 0.4, 'y': 0}
        button.bind(on_press=self.process_image)
        layout.add_widget(button)
        self.add_widget(layout)

    def on_pre_enter(self, *args):
        self.image.source = App.get_running_app().image_filename

    def process_image(self, event):
        process()



class CameraApp(App):

    image_filename = ''

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(CameraScreen(name='camera'))
        self.sm.add_widget(PreviewScreen(name='preview'))
        return self.sm

if __name__ == '__main__':
    CameraApp().run()
