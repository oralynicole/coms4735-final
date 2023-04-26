from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# Set different windows

class LoginWindow(Screen): 
    pass

class ImageCaptureWindow(Screen):
    pass

class VerificationWindow(Screen): 
    pass

class ConfirmationWindow(Screen): 
    pass

class WindowManager(ScreenManager): 
    pass

# Add your Builder to the kv file
kv= Builder.load_file("my.kv")

class MyMainApp(App): 
    def build(self): 
        return kv
    

if __name__ == "__main__": 
    MyMainApp().run()
 