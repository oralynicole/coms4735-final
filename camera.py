from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainCameraApp(App): 
    
    def build(self): 
    
        self.camera_obj = Camera()

        # Button 
        button_object = Button(text="Click Here")
        button_object.size_hint = (.5,.2)
        button_object.pos_hint = {'x': .25, 'y': .25}
        button_object.bind(on_press=self.take_image)

        # Layout 
        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_object)
        return layout
    
    def take_image(self, *args): 
        self.camera_obj.export_to_png("./selfie.png")

if __name__ == "__main__": 
    MainCameraApp().run()
