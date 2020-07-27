import ctypes
import time

import win32gui
import re

import pygetwindow as gw


hex_code_dict = {}
hex_code_dict['lmb'] = 0x01
hex_code_dict['rmb'] = 0x02
hex_code_dict['a'] = 0x41
hex_code_dict['a'] = 0x41
hex_code_dict['b'] = 0x42
hex_code_dict['c'] = 0x43
hex_code_dict['d'] = 0x44
hex_code_dict['e'] = 0x45
hex_code_dict['f'] = 0x46
hex_code_dict['g'] = 0x47
hex_code_dict['h'] = 0x48
hex_code_dict['i'] = 0x49
hex_code_dict['j'] = 0x4A
hex_code_dict['k'] = 0x4B
hex_code_dict['l'] = 0x4C
hex_code_dict['m'] = 0x4D
hex_code_dict['n'] = 0x4E
hex_code_dict['o'] = 0x4F
hex_code_dict['p'] = 0x50
hex_code_dict['q'] = 0x51
hex_code_dict['r'] = 0x52
hex_code_dict['s'] = 0x53
hex_code_dict['t'] = 0x54
hex_code_dict['u'] = 0x55
hex_code_dict['v'] = 0x56
hex_code_dict['w'] = 0x57
hex_code_dict['x'] = 0x58
hex_code_dict['y'] = 0x59
hex_code_dict['z'] = 0x5A
hex_code_dict['shift'] = 0x4B

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
# https://gist.github.com/dretax/fe37b8baf55bc30e9d63
# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# while (True):
#     PressKey()
#     time.sleep(1)
#     ReleaseKey(0x11)
#     time.sleep(1)

def type_string(word, window_mgr, window_name):
    w.find_window_wildcard(window_name)
    w.set_foreground()
    time.sleep(5)
    for letter in word:
        print(hex_code_dict[letter])
        PressKey(0x11)
        time.sleep(0.86)
        ReleaseKey(0x11)
        time.sleep(0.86)

#windows = gw.getAllTitles()

#print(windows)

print(type(0x11))

#exit(1)
#w = WindowMgr()
#type_string("test",w,'Sticky Notes')
    
