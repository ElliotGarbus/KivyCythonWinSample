from kivy.config import Config
from metadata import app_icon

# import os

# os.environ["KIVY_NO_FILELOG"] = "1"
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

"""
configstartup.py is for initial setup of the environment

This file MUST be imported at the top of the 'main' executable file.  
"""

Config.set('kivy', 'window_icon', app_icon)
Config.set('kivy', 'exit_on_escape', 0)
Config.set('input', 'mouse', 'mouse,disable_multitouch')
