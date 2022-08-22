from kivy.app import App
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
from kivy.core.window import Window

Window.size = (310, 580)
kv = '''
BoxLayout:
    orientation: 'vertical'
    Image:
        id: img1
        size_hint: 1.0, 0.7
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1.0, 0.1
'''

class CvCamera(App):
    def build(self):  # Construcción de interfaz de usuario, etc
        return self.check()

    def check(self):
        self._cap = cv2.VideoCapture(0)

        layout = Builder.load_string(kv)

        while not self._cap.isOpened():
            pass

        Clock.schedule_interval(self.update, 1.0 / 30.0)

        return layout


    def update(self, dt):
        ret, img = self._cap.read()
        img = cv2.flip(img, 0)
        texture1 = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')
        self.root.ids.img1.texture = texture1


if __name__ == '__main__':
   CvCamera().run()