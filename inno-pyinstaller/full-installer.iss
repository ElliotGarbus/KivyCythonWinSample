; Full Installation file Installes App + Service, App only or Service Only
; WIP see TODO at Bottom of file


#define MyAppName "My Application"
#define MyAppVersion "0.0"
#define MyAppExeName "MyApplication.exe"
#define AppDir "Application"

#define MySvcName "MyService"
#define MySvcVersion "0.0"
#define MyAppExeName "MyService.exe"
#define ServiceDir "Service"

#define MyAppPublisher "My Company, Inc."
#define MyAppURL "https://www.example.com/"


[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{3947807D-874C-49FC-B8CB-12882EAF84FF}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\MyCompany
DisableProgramGroupPage=yes
LicenseFile=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\LICENSE
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\inno-pyinstaller
OutputBaseFilename=full-installer
SetupIconFile=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\myapplication\asset\cropped-cactus-512x512.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
WizardSmallImageFile=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\myapplication\asset\small_installer_image_138x140.bmp
WizardImageFile=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\myapplication\asset\big_installer_image_410x797.bmp

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Types]
Name: "full"; Description: "Application and Service"
Name: "app-only"; Description: "Application Only"
Name: "service-only"; Description: "Service Only"

[Components]
Name: "application"; Description: "Application Files"; Types: full app-only
Name: "service"; Description: "Windows Service Files"; Types: full service-only


[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; Components: application

[Files]
; Application Files
Source: "C:\Users\ellio\PycharmProjects\KivyCythonWinSample\inno-pyinstaller\dist\MyApplication\{#MyAppExeName}"; DestDir: "{app}\{#AppDir}"; Flags: ignoreversion; Components: application
Source: "C:\Users\ellio\PycharmProjects\KivyCythonWinSample\inno-pyinstaller\dist\MyApplication\*"; DestDir: "{app}\{#AppDir}"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: application
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
; Service Files
Source: "C:\Users\ellio\PycharmProjects\KivyCythonWinSample\pyinstaller-service\dist\MyService\{#MySvcExeName}"; DestDir: "{app}\{#ServiceDir}"; Flags: ignoreversion; Components: service 
Source: "C:\Users\ellio\PycharmProjects\KivyCythonWinSample\pyinstaller-service\dist\MyService\*"; DestDir: "{app}\{#ServiceDir}"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: service 


[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Components: application
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Tasks: desktopicon; Components: application
Name: "{autoprograms}\{#MySvcName}"; Filename: "{app}\{#ServiceDir}\{#MySvcExeName}"; Components: service

[Run]
Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent; Components: application
Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Parameters: "install"; Description: "Register the Service"; Flags: runascurrentuser postinstall; Components: service


; TODO: check destination dirs for app and service
; TODO: And run unninstall to revome service
; TODO: Set DefaultGroupName
; TODO add Parameter for Service ICON to bring up UI
; TODO set service parameter intall and start service




