from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2 as cv
from playsound import playsound

Window.size = (310, 580)

help_str = '''

ScreenManager:
    
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    PreviewScreen:
    
    
<WelcomeScreen>:
    name: "welcome"
    md_bg_color: 0/255, 0/255, 0/255, 0
    FitImage:
        source:"assets/welcome.png"
    
    Button:
        text: "GET STARTED"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .15}
        background_color: 0,0,50,0
        font_name: "BPoppins"
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "main"
        canvas.before:
            Color:
                rgb: rgba(0,24,69,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20]
                
<MainScreen>:
    name: "main"
    md_bg_color: 0/255, 0/255, 0/255, 0
    FitImage:
        source:"assets/backgroundd.png"
    
    MDLabel:
        text: "Security at your Finger-tip!"
        font_name: "MPoppins"
        font_size: "13sp"
        size_hint_x: .85
        pos_hint: {"center_x": .52, "center_y": .3}
        halign: "center"
        color: rgba(255,255,255,255)
    Button:
        text: "LOGIN"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .18}
        background_color: 0,0,50,0
        font_name: "BPoppins"
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "login"
        canvas.before:
            Color:
                rgb: rgba(0,24,69,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
                
    Button:
        text: "SIGNUP"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .09}
        background_color: 35,99,203,0
        font_name: "BPoppins"
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "signup"
        canvas.before:
            Color:
                rgb: rgba(20,55,100,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
                
<LoginScreen>:
    name: "login"
    md_bg_color: 0/255, 0/255, 0/255, 0
    FitImage:
        source:"assets/main-bg.png"
    MDFloatLayout:
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y":.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(255,255,255,255)
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
        background_color: 0,0,50,0
        font_name: "BPoppins"
        on_release:
            app.get_data(email.text,password.text)


        canvas.before:
            Color:
                rgb: rgba(0,24,69,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
    
    MDLabel:
        text: "Don't have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .68, "center_y": .28}
        color: rgba(135,133,193,255)

    MDTextButton:
        text: "Sign up"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .75, "center_y": .28}
        color: rgba(30,95,100,255)
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "signup"
    
<SignupScreen>:
    name:"signup"
    md_bg_color: 0/255, 0/255, 0/255, 0
    FitImage:
        source:"assets/main-bg.png"
    MDFloatLayout:
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y":.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(255,255,255,255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "main"
    MDLabel:
        text: "Hi There !"
        font_name: "BPoppins"
        font_size: "23sp"
        pos_hint: {"center_x": .6,"center_y": .90}
        color: rgba(255,255,255,255)
    MDLabel:
        text: "Create a new Account"
        font_name: "MPoppins"
        font_size: "18sp"
        pos_hint: {"center_x": .6, "center_y": .85}
        color: rgba(135, 135, 193 ,255)
        
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .76}
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
        pos_hint: {"center_x": .5, "center_y": .68}
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
            
    MDLabel:
        text: " Camera Info"
        color: rgba(225,225,225,255)
        pos_hint: {"center_x": .45,"center_y":.56}
        font_size: "15sp"
        font_name: "BPoppins"
        halign: "center"
    MDFloatLayout:
        md_bg_color: rgba(178,178,178,255)
        size_hint: .17,.001
        pos_hint: {"center_x": .2, "center_y": .560}
    MDFloatLayout:
        md_bg_color: rgba(178,178,178,255)
        size_hint: .19,.001
        pos_hint: {"center_x": .72, "center_y": .560}
        
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .48}
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
        pos_hint: {"center_x": .5, "center_y": .40}
        TextInput:
            id: userpassword
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
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
            
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .32}
        TextInput:
            id: ipaddress
            hint_text: "IpAddress"
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
    
    


    Button:
        text: "SIGNUP"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .2}
        background_color: 0,0,50,0
        font_name: "BPoppins"
        on_release: app.send_data(email.text,password.text,username.text,userpassword.text,ipaddress.text)
        canvas.before:
            Color:
                rgb: rgba(0,24,69,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
    
    MDLabel:
        text: "Already have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .68, "center_y": .14}
        color: rgba(135,133,193,255)

    MDTextButton:
        text: "Sign in"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .79, "center_y": .14}
        color: rgba(30,95,100,255)
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "login"
            
<PreviewScreen>:
    name:"preview"
    md_bg_color: 0/255, 0/255, 0/255, 0
    FitImage:
        source:"assets/main-bg.png"
    BoxLayout:
        Cam:
            id: cam1
    MDLabel:
        id: rtsp_link
        text: "RTSP Link"
        font_name: "BPoppins"
        font_size: "13sp"
        halign: "center"
        pos_hint: {"center_y":.16}
        color: rgba(135,133,193,255)
  

'''


class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class PreviewScreen(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name = 'welcome'))
screen_manager.add_widget(MainScreen(name = 'main'))
screen_manager.add_widget(LoginScreen(name = 'login'))
screen_manager.add_widget(SignupScreen(name = 'signup'))

rtsp = ['rtsp://admin:123456@192.168.1.208:554']
class Cam(Image):
    def on_kv_post(self, base_widget):
        # self.capture = cv.VideoCapture(0)
        # print(rtsp)
        self.capture = cv.VideoCapture(rtsp[-1])
        print(rtsp)
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


class Main(MDApp):


    def build(self):
        self.strng = Builder.load_string(help_str)
        return self.strng




    def send_data(self, email, password, username,userpassword,ipaddress):


        from firebase import firebase

        # Initialize Firebase
        firebase = firebase.FirebaseApplication('https://spy-bound-59012-default-rtdb.firebaseio.com/', None)

        # Importing Data
        data = {
            'Email': email,
            'Password': password,
            'Username': username,
            'Upassword': userpassword,
            'IpAddress': ipaddress
        }

        # Post Data
        # Database Name/Table
        firebase.post('spy-bound-59012-default-rtdb/Users', data)
        print("Done")
        self.strng.get_screen('preview').manager.current = 'preview'


        return ''

    def get_data(self, email, password):



        from firebase import firebase

        # Initialize Firebase
        firebase = firebase.FirebaseApplication('https://spy-bound-59012-default-rtdb.firebaseio.com/', None)

        # Get Data
        result = firebase.get('spy-bound-59012-default-rtdb/Users','')
        # print(result)
        flag=False
        # Get Specific column like email or password
        j = 0
        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    flag=True
                    j = i
                    break


        if(flag):
            self.screen_manager = ScreenManager()
            print(email + " Logged In!")
            print(result[i]['IpAddress'])
            rtsp.append("rtsp://{}:{}@{}:554".format(result[i]['Username'],result[i]['Upassword'],result[i]['IpAddress']))
            # sound = SoundLoader.load('assets/alert.mpeg')
            # if sound:
            #     sound.play()
            playsound('assets/alert.mpeg')
            self.strng.get_screen('preview').ids.rtsp_link.text = rtsp[-1]
            self.strng.get_screen('preview').manager.current = 'preview'

        else:
            print("Invalid credentials")

        return ''



if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="D:/spyBound/fonts/fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="D:/spyBound/fonts/fonts/Poppins-SemiBold.ttf")

    Main().run()