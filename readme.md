**KWin Wayland mouse handedness control**

This script switches between left handed / right handed mode for all input devices on the system. It uses KWin's DBus API to do this in KDE Wayland session.

I find that regularly switching between the left/right hand is helpful for reducing wrist/hand strain.

---

*Note: if you're using X11 (with any DE/WM), you can instead do:*

```
xmodmap -e "pointer = 1 2 3"   # right handed
xmodmap -e "pointer = 3 2 1"   # left handed
```

---

**Usage**

First, install the `pydbus` package:

- Arch Linux: `pacman -S python-pydbus`
- Others: `pip3 install --user pydbus`

Then, invoke the script with "l" or "r" as the argument:

```
./kwin-wayland-mouse-handedness-control.py r
./kwin-wayland-mouse-handedness-control.py l
```

Note: This script only attempts to operate on devices `/dev/input/event{0-99}`. If you have a huge number of input devices connected, you'll need to increase the range in the script.

---

**Adding shortcuts to taskbar**

You can add shortcut buttons to your taskbar to switch between left/right handedness.

- Add a Quicklaunch widget to your taskbar

- Right click the new quicklaunch widget => Configure Quicklaunch
	- Enable 'Show launcher names'

- Repeat these next steps for left and right:
	- Right click the new quicklaunch widget => Add Launcher
		- Click the browse button and select the kwin-wayland-mouse-handeness-control.py script. A shortcut for it will be added to the quicklaunch.
	- Right click the newly addded launcher/shortcut => Edit Launcher
		- In the Application tab:
			- Change the name to "l" or "r" (to show the letter in the quicklaunch widget)
			- Append " l" or " r" to the Command, to invoke the script with an argument


Note: In the General tab of "Edit Launcher", the name corresponds to the filename in `~/.local/share/applications/*.desktop` for this shortcut. There's no need to change it, KDE will automatically create a unique filename for the second entry.
