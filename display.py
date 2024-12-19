import sys
import gi
import subprocess
from datetime import datetime
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib, Gdk, Gio, GdkPixbuf

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(1280,720)

        self.auto_sleep = "On"

        self.outer_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.outer_box.set_spacing(10)
        self.outer_box.set_margin_top(20)
        self.outer_box.set_margin_start(20)
        self.outer_box.set_margin_end(20)
        self.outer_box.set_margin_bottom(20)

        # top_box houses datetime_box and Display Buttons
        self.top_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        self.top_box.set_spacing(10)
        self.top_box.set_halign(Gtk.Align.FILL)
        self.top_box.set_vexpand(False)

        self.suspend_display_button = Gtk.Button()
        self.suspend_display_button.set_valign(Gtk.Align.START)
        self.suspend_display_button.set_size_request(100, 100)
        self.suspend_display_button.connect('clicked', self.suspend_display)

        self.suspend_display_icon = Gtk.Image.new_from_paintable(Gdk.Texture.new_for_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_scale("/home/will/gitrepos/tv-controller/icons/moon-outline-symbolic.svg",100,100,True)))
        self.suspend_display_button.set_child(self.suspend_display_icon)

        ## datetime_box houses date and time labels
        self.datetime_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        self.date_label = Gtk.Label()
        self.date_label.set_halign(Gtk.Align.CENTER)
        self.date_label.set_opacity(0.5)
        self.time_label = Gtk.Label()
        self.time_label.set_markup(f'<span size="131072" weight="bold">--:--</span>')
        self.time_label.set_halign(Gtk.Align.CENTER)
        self.time_label.set_hexpand(True)

        self.datetime_box.append(self.date_label)
        self.datetime_box.append(self.time_label)
        ##

        self.toggle_auto_sleep_button = Gtk.Button(label="Auto-Sleep\nOn")
        self.toggle_auto_sleep_button.set_valign(Gtk.Align.START)
        self.toggle_auto_sleep_button.set_size_request(100, 100)
        self.toggle_auto_sleep_button.connect('clicked', self.toggle_auto_sleep)

        self.top_box.append(self.suspend_display_button)
        self.top_box.append(self.datetime_box)
        self.top_box.append(self.toggle_auto_sleep_button)

        # bottom_box houses buttons and Now Playing Data
        self.bottom_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        self.bottom_box.set_spacing(10)
        self.bottom_box.set_halign(Gtk.Align.BASELINE)
        self.bottom_box.set_vexpand(True)

        self.outer_toast = Adw.ToastOverlay()

        self.outer_box.append(self.top_box)
        self.outer_box.append(self.bottom_box)

        self.outer_toast.set_child(self.outer_box)
        self.set_child(self.outer_toast)
        
        GLib.timeout_add_seconds(1, self.update_datetime)

    def update_datetime(self):
        # Get the current time and update the label
        current_date = datetime.now().strftime("%A %d %B")
        current_time = datetime.now().strftime("%H:%M")
        self.date_label.set_markup(f'<span size="32768">{current_date}</span>')
        self.time_label.set_markup(f'<span size="131072" weight="bold">{current_time}</span>')
        return True  # Return True to keep the timeout running

    def suspend_display(self, button):
        try:
            subprocess.run(["xset", "dpms", "force", "off"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to put display to sleep: {e}")
        else:
            print("Putting display to sleep")

    def toggle_auto_sleep(self, button):
        try:
            if self.auto_sleep == "On":
                # If auto_sleep is on, turn auto_sleep off, set to false
                subprocess.run(["xset", "-dpms"], check=True)
                self.auto_sleep = "Off"
            else:
                subprocess.run(["xset", "dpms", "10", "10", "10"], check=True)
                self.auto_sleep = "On"

            self.auto_sleep_toast = Adw.Toast(title=f"Auto-Sleep toggled {self.auto_sleep}", priority=Adw.ToastPriority.HIGH, timeout=2)
            self.outer_toast.add_toast(self.auto_sleep_toast)

            self.toggle_auto_sleep_button.set_label(f"Auto-Sleep\n{self.auto_sleep}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to toggle display auto sleep: {e}")
        else:
            print(f"Changed display auto sleep to {self.auto_sleep}")


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

        sm = app.get_style_manager()
        sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
