
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from cvcamera import CvCamera


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

Window.size = (310, 580)

help_str = '''
ScreenManager:
    
    MainScreen:
    LoginScreen:
    SignupScreen:
    DashboardScreen:
    HomeScreen:
    PreviewScreen:
    Preview2Screen:
    
    
<MainScreen>:
    name: "main"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: "assets/logo.jpg"
            size_hint: .16, .16
            pos_hint: {"center_x": .12, "center_y": .95}
        Image:
            source: "assets/back.png"
            size_hint: 2, 2
            pos_hint: {"center_x": .53, "center_y": .67}
        MDLabel:
            text: "H e l l o  !"
            font_name: "BPoppins"
            font_size: "23sp"
            pos_hint: {"center_y": .38}
            halign: "center"
            color: rgba(34,34,34,255)
        MDLabel:
            text: "Best place to write life stories and share your journey experiences"
            font_name: "MPoppins"
            font_size: "13sp"
            size_hint_x: .85
            pos_hint: {"center_x": .52, "center_y": .3}
            halign: "center"
            color: rgba(34,34,34,255)
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            background_color: 0,0,0,0
            font_name: "BPoppins"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "login"
            canvas.before:
                Color:
                    rgb: rgba(52,0,231,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
        Button:
            text: "SIGNUP"
            size_hint: .67, .065
            pos_hint: {"center_x": .5, "center_y": .09}
            background_color: 0,0,0,0
            font_name: "BPoppins"
            color: rgba(52,0,231,255)
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "signup"
            canvas.before:
                Color:
                    rgb: rgba(52,0,231,255)
                Line:
                    width: 1.2
                    rounded_rectangle: self.x, self.y, self.width, self.height,5,5,5,5,100
                    
<HomeScreen>:
    name:"home"
    MDLabel:
        text: "Welcome Back !"
        font_name: "BPoppins"
        font_size: "23sp"
        pos_hint: {"center_x": .6,"center_y": .85}
        color: rgba(0,0,59,255)
        
    
        
<DashboardScreen>:
    name:"dashboard"
    MDLabel:
        text: "Welcome to Dashboard !"
        font_name: "BPoppins"
        font_size: "23sp"
        pos_hint: {"center_x": .6,"center_y": .85}
        color: rgba(0,0,59,255)
    
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .63}
        TextInput:
            id: uname
            hint_text: "Username"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)

    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .5}
        TextInput:
            id: password
            hint_text: "Password"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .4}
        TextInput:
            id: ipaddress
            hint_text: "IpAddress"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .4}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)

    Button:
        text: "SUBMIT"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .30}
        background_color: 0,0,0,0
        font_name: "BPoppins"
        on_release:
            app.camera_setup(uname.text,password.text,ipaddress.text)


        canvas.before:
            Color:
                rgb: rgba(52,0,231,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]

<LoginScreen>:
    name: "login"
    id: "login"
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y":.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26,24,58,255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "main"
    MDLabel:
        text: "W e l c o m e  !"
        font_name: "BPoppins"
        font_size: "23sp"
        pos_hint: {"center_x": .6,"center_y": .85}
        color: rgba(0,0,59,255)
    MDLabel:
        text: "Sign in to continue"
        font_name: "MPoppins"
        font_size: "18sp"
        pos_hint: {"center_x": .6, "center_y": .79}
        color: rgba(135, 135, 193 ,255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .63}
        TextInput:
            id: email
            hint_text: "Email"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)

    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .5}
        TextInput:
            id: password
            hint_text: "Password"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)

    Button:
        text: "LOGIN"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .34}
        background_color: 0,0,0,0
        font_name: "BPoppins"
        on_release:
            app.get_data(email.text,password.text)


        canvas.before:
            Color:
                rgb: rgba(52,0,231,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
    MDTextButton:
        text: "Forgot Password?"
        pos_hint: {"center_x": .5, "center_y": .28}
        color: rgba(68,78,132,255)
        font_size: "12sp"
        font_name: "BPoppins"
    MDLabel:
        text: "or"
        color: rgba(52,0,231,255)
        pos_hint: {"center_y":.22}
        font_size: "13sp"
        font_name: "BPoppins"
        halign: "center"
    MDFloatLayout:
        md_bg_color: rgba(178,178,178,255)
        size_hint: .3,.002
        pos_hint: {"center_x": .3, "center_y": .218}
    MDFloatLayout:
        md_bg_color: rgba(178,178,178,255)
        size_hint: .3,.002
        pos_hint: {"center_x": .7, "center_y": .218}
    MDLabel:
        text: "Social Media Login"
        font_name: "BPoppins"
        font_size: "13sp"
        halign: "center"
        pos_hint: {"center_y":.16}
        color: rgba(135,133,193,255)
    MDGridLayout:
        cols: 2
        size_hint: .43, .05
        pos_hint: {"center_x": .5, "center_y": .1}
        Image:
            source: "assets/google.png"
        Image:
            source: "assets/meta.png"
    MDLabel:
        text: "Don't have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .68, "center_y": .04}
        color: rgba(52,0,231,255)

    MDTextButton:
        text: "Sign up"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .75, "center_y": .04}
        color: rgba(135,133,193,255)
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "signup"
    
<SignupScreen>:
    name:"signup"
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y":.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26,24,58,255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "main"
    MDLabel:
        text: "H i !"
        font_name: "BPoppins"
        font_size: "23sp"
        pos_hint: {"center_x": .6,"center_y": .85}
        color: rgba(0,0,59,255)
    MDLabel:
        text: "Create a new account"
        font_name: "MPoppins"
        font_size: "18sp"
        pos_hint: {"center_x": .6, "center_y": .79}
        color: rgba(135, 135, 193 ,255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .68}
        TextInput:
            id: username
            hint_text: "Username"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .56}
        TextInput:
            id: email
            hint_text: "Email"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)

    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .44}
        TextInput:
            id: password
            hint_text: "Password"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x":.43, "center_y": .5}
            background_color: 1,1,1,0
            foreground_color: rgba(0,0,59,255)
            cursor_color: rgba(0,0,59,255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    Button:
        text: "SIGNUP"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .3}
        background_color: 0,0,0,0
        font_name: "BPoppins"
        on_release: app.send_data(username.text,email.text,password.text)
        canvas.before:
            Color:
                rgb: rgba(52,0,231,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
    MDLabel:
        text: "or"
        color: rgba(52,0,231,255)
        pos_hint: {"center_y":.22}
        font_size: "13sp"
        font_name: "BPoppins"
        halign: "center"
    MDFloatLayout:
        md_bg_color: rgba(178,178,178,255)
        size_hint: .3,.002
        pos_hint: {"center_x": .3, "center_y": .218}
    MDFloatLayout:
        md_bg_color: rgba(178,178,178,255)
        size_hint: .3,.002
        pos_hint: {"center_x": .7, "center_y": .218}
    MDLabel:
        text: "Social Media Login"
        font_name: "BPoppins"
        font_size: "13sp"
        halign: "center"
        pos_hint: {"center_y":.16}
        color: rgba(135,133,193,255)
    MDGridLayout:
        cols: 2
        size_hint: .43, .05
        pos_hint: {"center_x": .5, "center_y": .1}
        Image:
            source: "assets/google.png"
        Image:
            source: "assets/meta.png"
    MDLabel:
        text: "Already have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .68, "center_y": .04}
        color: rgba(135,133,193,255)

    MDTextButton:
        text: "Sign in"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .79, "center_y": .04}
        color: rgba(52,0,231,255)
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "login"
            
<PreviewScreen>:
    name:"preview"
    MDLabel:
        id: rtsp_link
        text: "RTSP Link"
        font_name: "BPoppins"
        font_size: "13sp"
        halign: "center"
        pos_hint: {"center_y":.16}
        color: rgba(135,133,193,255)
        
    BoxLayout:
        Image:
            id: img2
            
<Preview2Screen>:
    name: "preview2"
    BoxLayout:
        orientation: 'vertical'
        Image:
            id: img1
            size_hint: 1.0, 0.7
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1.0, 0.1


        '''

class DashboardScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class HomeScreen(Screen):
    pass

class PreviewScreen(Screen):
    pass

class Preview2Screen(Screen):
    pass
screen_manager = ScreenManager()
screen_manager.add_widget(HomeScreen(name = 'home'))
screen_manager.add_widget(MainScreen(name = 'main'))
screen_manager.add_widget(LoginScreen(name = 'login'))
screen_manager.add_widget(SignupScreen(name = 'signup'))
screen_manager.add_widget(DashboardScreen(name = 'dashboard'))
screen_manager.add_widget(PreviewScreen(name = 'preview'))
screen_manager.add_widget(Preview2Screen(name = 'preview2'))




class Slope(MDApp):

    global link
    link = 0

    def build(self):
        self.strng = Builder.load_string(help_str)
        return self.strng

    def get_data(self, email, password):



        from firebase import firebase

        # Initialize Firebase
        firebase = firebase.FirebaseApplication('https://spy-bound-59012-default-rtdb.firebaseio.com/', None)

        # Get Data
        result = firebase.get('spy-bound-59012-default-rtdb/Users','')
        # print(result)
        flag=False
        # Get Specific column like email or password
        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    flag=True


        if(flag):
            self.screen_manager = ScreenManager()
            print(email + " Logged In!")
            self.strng.get_screen('home').manager.current = 'home'
        else:
            print("Invalid credentials")

        return ''

    # def get_user(self,email, password):
    #     self.get_data(email,password)
    #     root.manager.current = "home"



    def send_data(self, username, email, password):


        from firebase import firebase

        # Initialize Firebase
        firebase = firebase.FirebaseApplication('https://spy-bound-59012-default-rtdb.firebaseio.com/', None)

        # Importing Data
        data = {
            'Username': username,
            'Email': email,
            'Password': password
        }

        # Post Data
        # Database Name/Table
        firebase.post('spy-bound-59012-default-rtdb/Users', data)
        self.strng.get_screen('dashboard').manager.current = 'dashboard'


        return ''

    def camera_setup(self,uname,password,ipaddress):
        from firebase import firebase

        # Initialize Firebase
        firebase = firebase.FirebaseApplication('https://spy-bound-59012-default-rtdb.firebaseio.com/', None)

        # Importing Data
        data = {
            'Username': uname,
            'Password': password,
            'Ipaddress': ipaddress
        }

        firebase.post('spy-bound-59012-default-rtdb/CameraInfo', data)
        link = f"rtsp://{uname}:{password}@{ipaddress}:554"
        # cv = CvCamera()
        # cv.check()
        # self.strng.get_screen('preview').ids.rtsp_link.text = link
        # self.camera_util(link)

        self.strng.get_screen('preview2').manager.current = 'preview2'
        self.check()

        return ''

    def check(self):
        self._cap = cv2.VideoCapture(0)

        # layout = Builder.load_string()

        while not self._cap.isOpened():
            pass

        Clock.schedule_interval(self.update, 1.0 / 30.0)

        return ''


    def update(self, dt):
        ret, img = self._cap.read()
        img = cv2.flip(img, 0)
        texture1 = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')
        # Clock.schedule_interval(self.root.img1.texture, 1 / 60.)
        self.root.ids.img1.texture = texture1








if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="D:/spyBound/fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="D:/spyBound/fonts/Poppins-SemiBold.ttf")

    Slope().run()









