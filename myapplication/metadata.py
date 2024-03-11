# one location for version information and file assignments
# used by kivy, pyinstaller and inno-setup
# execute: python metadata.py to create metadata.txt that will be imported by
# inno-pyinstaller/full-installer.iss to set the meta-data for the installer

company = "MyCompany"

app_name = "MyApplication"
app_version = '0.0'
app_name_version = f'{app_name} v{app_version}'
app_icon = 'asset/cropped-cactus-512x512.ico'

service_name = "MyService"
service_version = '0.0'
service_name_version = f'{service_name} v{service_version}'
service_icon = 'asset/service_setting_512x512.ico'

library_version = '0.0.0'  # used in setup.py to set the version of the library

# the values below are only used by innosetup
app_dir = 'Application'  # this is a subdirectory under the Windows programs dir, where the app is installed
service_dir = 'Service'  # this is a subdirectory under the Windows programs dir, where the service is installed
startup_menu_group = 'My Company'  # name of the startup menu folder that holds the app + service
publisher = 'My Company, Inc.'
company_url = 'https://www.example.com/'

if __name__ == '__main__':
    # run this file to create the metadata for inno setup
    from pathlib import Path
    from textwrap import dedent

    project_path = str(Path(__file__).parent.parent)  # used in innosetup to set the 'root' path of the project

    defines = dedent(f"""
                     ;file created by metadata.py
                     #define MyAppName "{app_name}"
                     #define MyAppVersion "{app_version}"
                     #define MyAppExeName "{app_name}.exe"
                     #define AppDir "{app_dir}"  ; sub-dir where app is installed on client machine
                     
                     #define MySvcName "{service_name}"
                     #define MySvcVersion "{service_version}"
                     #define MySvcExeName "{service_name}.exe"
                     #define ServiceDir "{service_dir}"  ; sub-dir where service is installed on client machine
                     
                     #define ProjectPath "{project_path}"
                     #define StartUpMenuGroup "{startup_menu_group}"
                     #define MyAppPublisher "{publisher}"
                     #define MyAppURL "{company_url}"
                     """)

    print('Creating Metadata file for inno setup file: inno-pyinstaller/full-installer.iss')
    print(defines)

    with open('../inno-pyinstaller/metadata.txt', 'wt') as f:
        f.write(defines)
