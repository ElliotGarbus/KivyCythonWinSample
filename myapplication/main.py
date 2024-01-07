import os
import sys
#os.environ["KIVY_NO_FILELOG"] = "1"
#os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.app import App
from kivy.lang import Builder

# FIXME: Need a real solution for "import mylibrary" here
# In the Cython/Pyinstaller example it seems the approach is
# to make everything installable package, but I don't know
# if it's the best approach. Adapt as needed.
sys.path.insert(0, "..")
from mylibrary import ProprietaryClass
from mylibrary.subdir import MyLib_Constants

class ProprietaryApp(App):
    def build(self):
        self.icon = "asset/32x32.ico"
        self._secret = ProprietaryClass()
        # EVALUATE: Ideally this metadata does not need to be hardcoded, but
        # can be obtained from the build system. For example generate a .py
        # file, or supply the values via os.environ[], or some other solution.
        # If this can't be practically accomplished, communicate the 
        company = "MyCompany"
        appname = "MyApplication"
        appversion = 1.0
        print(f"Config file path: %AppData%/{company}/{appname}/v{appversion}/config.json")
        print(f"Library constants: {MyLib_Constants}")
        return Builder.load_file("main.kv")
        
    def secret_stuff(self):
        return self._secret.hello_world()

if __name__ == '__main__':
    ProprietaryApp().run()