import configstartup  # must load before kivy, sets env vars/config
from kivy.app import App
from kivy.lang import Builder
from metadata import app_icon, company, app_name, app_version

from mylibrary import ProprietaryClass
from mylibrary.subdir import MyLib_Constants


class ProprietaryApp(App):
    def build(self):
        self.icon = app_icon
        self.title = f'{app_name} v{app_version}'
        self._secret = ProprietaryClass()
        print(f"Config file path: %AppData%/{company}/{app_name}/v{app_version}/config.json")
        print(f"Library constants: {MyLib_Constants}")
        return Builder.load_file("main.kv")

    def secret_stuff(self):
        return self._secret.hello_world()

    def open_settings(self, *largs):
        """This disables opening the kivy control panel"""
        pass


if __name__ == '__main__':
    ProprietaryApp().run()
