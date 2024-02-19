; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "MyService"
#define MyAppVersion "0.0"
#define MyAppPublisher "My Company, Inc."
#define MyAppURL "https://www.example.com/"
#define MyAppExeName "MyService.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E6000DBB-B59F-464F-BBC8-BF16A4FF1B1D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\MyCompany\MyService
DisableProgramGroupPage=yes
LicenseFile=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\LICENSE
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\inno-pyinstaller
OutputBaseFilename=service-installer
SetupIconFile=C:\Users\ellio\PycharmProjects\KivyCythonWinSample\myapplication\asset\service_setting_512x512.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\Users\ellio\PycharmProjects\KivyCythonWinSample\pyinstaller-service\dist\MyService\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\ellio\PycharmProjects\KivyCythonWinSample\pyinstaller-service\dist\MyService\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Parameters: "install"; Description: "Register the Service"; Flags: runascurrentuser postinstall;


