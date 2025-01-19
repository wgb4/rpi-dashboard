from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition.transition import MDSharedAxisTransition
from datetime import datetimed
import subprocess
from rpi_backlight import Backlight
import threading
from cec_control import CecProcess

Window.rotation = 270
Window.fullscreen = True
Window.size = (1280, 720)

backlight = Backlight()
cec_process = CecProcess()

class DashboardScreen(MDScreen):
    pass

class TimeoutScreen(MDScreen):
    pass

class Dashboard(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Navy"

        self.sm = MDScreenManager()
        self.sm.transition = MDSharedAxisTransition()
        self.sm.add_widget(DashboardScreen(name='dashboard'))
        self.sm.add_widget(TimeoutScreen(name='timeout'))

        Clock.schedule_interval(self.update_time_date, 1)

        self.timeout_duration = 30
        self.timeout_event = Clock.schedule_once(self.to_sleep, self.timeout_duration)

        backlight.brightness = 100

        return self.sm
    
    def update_time_date(self, *args):
        current_screen = self.sm.get_screen(self.sm.current)
        current_screen.ids.time_label.text = datetime.now().strftime("%H:%M")
        current_screen.ids.date_label.text = datetime.now().strftime("%a %d %b")

    def reset_timeout(self, *args):
        # Cancel the current timeout event
        self.timeout_event.cancel()
        # Schedule a new timeout
        self.timeout_event = Clock.schedule_once(self.to_sleep, self.timeout_duration)

    def to_sleep(self, *args):
        self.sm.current = 'timeout'

        def fade_brightness():
            with backlight.fade(duration=0.2):
                backlight.brightness = 2

        # Run the brightness fade in a separate thread
        threading.Thread(target=fade_brightness).start()
        
    def wake_up(self, *args):
        self.sm.current = 'dashboard'
        self.reset_timeout()

        def fade_brightness():
            with backlight.fade(duration=0.2):
                backlight.brightness = 100

        # Run the brightness fade in a separate thread
        threading.Thread(target=fade_brightness).start()
        

    def start_moonlight(self):
        print("starting moonlight")
        return subprocess.Popen(
            ["moonlight-qt", "stream", "192.168.68.11", "Desktop"],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True,
            bufsize = 1
        )

Dashboard().run()