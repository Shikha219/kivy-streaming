import cv2 as cv

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

kv = """
#:kivy 1.11.0

<MenuScreen>:
    MainWidget:


<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'

        Cam:
            id: cam1

        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'settings'

ScreenManager:
    MenuScreen:
        name: 'menu'
    SettingsScreen:
        name: 'settings'
"""


class MainWidget(Widget):

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("\nmainwidget:")
        btnnext = Button(text='go to next', pos=(200, 400))
        btnnext.bind(on_press=self.gonext)
        self.add_widget(btnnext)

    # def savecard(self, btn_instance):

    def gonext(self, btn_inst):
        app = App.get_running_app()
        app.root.current = "settings"


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Cam(Image):

    def on_kv_post(self, base_widget):
        self.capture = cv.VideoCapture(0)
        # cv.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0 / 33.0)

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        # cv.imshow("CV2 Image", frame)

        # convert it to texture
        adaptive_thresh = frame

        buf1 = cv.flip(adaptive_thresh, 0)
        buf = buf1.tobytes()
        texture1 = Texture.create(size=(adaptive_thresh.shape[1], adaptive_thresh.shape[0]),
                                  )  # in grayscale gibts kein bgr
        # if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr')  # replacing texture
        # display image from the texture
        self.texture = texture1


class TestApp(App):

    def build(self):
        Window.clearcolor = (0, 0, 0.3, 1)
        return Builder.load_string(kv)


if __name__ == '__main__':
    TestApp().run()

