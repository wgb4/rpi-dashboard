What is this?
-
I've been experimenting with my raspberry pi connected to a tv, and came across a protocol called CEC that comes with the HDMI standard, this allows the raspberry pi to connect and perform basic controls (turn on / off) to the tv and devices connected to the tv as well (like consoles)

This made me think about creating an Apple CarPlay looking dashboard interface using a GTK and Adwaita design for a Raspberry Pi Touchscreen 2 that would include basic controls to the connected HDMI CEC devices, basic widgets like 'Now Playing' for my shairport-sync sound system (perhaps with playback controls if I can figure it out)

I also have a headless linux PC running Pop!_OS that I use for game streaming, I want the dashboard to control the PC (start Steam or games) and start a Moonlight stream to the PC. I use USBIP with a Bluetooth USB adapter to send controllers and a bluetooth speaker to the headless PC, I want a single button to be able to start the USBIP passthrough, load the stream, and connect the bluetooth speaker to the PC.

Useful Links:
-
PyGObject Docs:
https://pygobject.gnome.org

GNOME Python API Docs:
https://amolenaar.pages.gitlab.gnome.org/pygobject-docs/index.html

Required Packages:
-
(Following https://pygobject.gnome.org/getting_started.html)

For Raspberry Pi OS (Ubuntu / Debian):

`sudo apt install git python3-gi python3-gi-cairo gir1.2-gtk-4.0 libadwaita-1-dev xserver-xorg-core xserver-xorg-input-evdev xinit x11-xserver-utils xserver-xorg-input-libinput`

Whats installed:
- Basic X11 Envrionment with input support and utilities
- Gtk and Adwaita libraries and python packages

Using Raspberry Pi OS Lite with a basic X display:
-
This will made a kiosk environment where one app is displayed

  To allow ssh users to run `startx`:
  
  - Edit Xwrapper.config: `sudo nano /etc/X11/Xwrapper.config`
    
  - Change allowed_users to `anybody`


  To rotate the display output:
  
  - Edit ~/.xinitrc: `nano ~/.xinitrc`
  
  - Add: `xrandr --output DSI-1 --rotate left`
  
  - (Add: `python3 <PATH/TO/display.py>` for gui to auto start when `startx` is ran)
  

  To rotate the touchscreen input:
  
  - Edit the xorg libinput file in directory: `sudo nano /usr/share/X11/xorg.conf.d/40-libinput.conf`
  
  - Find the section that has 'touchscreen' and add the following inside the Section:
  
    `Option "TransformationMatrix" "0 -1 1 1 0 0 0 0 1"`
  
