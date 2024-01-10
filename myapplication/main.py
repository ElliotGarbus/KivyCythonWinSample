import configstartup  # must load before kivy, sets env vars/config
from kivy.app import App
from kivy.lang import Builder
from metadata import app_icon, company, app_name, app_version

from pathlib import Path
import os

from mylibrary import ProprietaryClass
from mylibrary.subdir import MyLib_Constants


class ProprietaryApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._secret = None  # secret lib object
        self._data_dir = None  # caches the path to the data directory

    def build(self):
        self.icon = app_icon
        self.title = f'{app_name} v{app_version}'
        self._secret = ProprietaryClass()
        print(f"Config file path: %AppData%/{company}/{app_name}/v{app_version}/config.json")
        print(f"Library constants: {MyLib_Constants}")
        print(f'{self.data_dir=}')
        return Builder.load_file("main.kv")

    def secret_stuff(self):
        return self._secret.hello_world()

    def open_settings(self, *largs):
        """This disables opening the kivy control panel"""
        pass

    def _get_data_dir(self):
        """
        Returns a path object to the app data directory
        %AppData%/{company}/{app_name}/v{app_version}/config.json"
        use the property App.data_dir
        """
        win_app_data = os.getenv('APPDATA')
        dd = Path(win_app_data) / f'{company}/{app_name}/v{app_version}'
        return dd

    @property
    def data_dir(self):
        if self._data_dir is None:
            self._data_dir = self._get_data_dir()
        return self._data_dir


if __name__ == '__main__':
    ProprietaryApp().run()
