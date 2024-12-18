Using Raspberry Pi OS Lite with a basic X display:

  To allow ssh users to run `startx`:
  
  - Edit Xwrapper.config: `sudo nano /etc/X11/Xwrapper.config`
    
  - Change allowed_users to `anybody`


  To rotate the display output:
  
  - Edit ~/.xinitrc: `nano ~/.xinitrc`
  
  - Add: `xrandr --output DSI-1 --rotate left`
  
  - (Add: `python3 <PATH/TO/display.py>` for gui to auto start when `startx` is ran)
  

  To rotate the touchscreen input:
  
  - Edit the xorg libinput file in directory: `cd /usr/share/X11/xorg.conf.d/`
  
  - Find the section that has 'touchscreen' and add the following inside the Section:
  
    `Option "TransformationMatrix" "0 -1 1 1 0 0 0 0 1"`
  
