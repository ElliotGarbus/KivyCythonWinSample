; Full Installation file - Installs App + Service, App only or Service Only
; WIP see TODO at Bottom of file


;#define MyAppName "My Application"
;#define MyAppVersion "0.0"
;#define MyAppExeName "MyApplication.exe"
;#define AppDir "Application"

;#define MySvcName "MyService"
;#define MySvcVersion "0.0"
;#define MySvcExeName "MyService.exe"
;#define ServiceDir "Service"

;#define StartUpMenuGroup "My Company"
;#define MyAppPublisher "My Company, Inc."
;#define MyAppURL "https://www.example.com/"
#include "metadata.txt"

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
DefaultGroupName={#StartUpMenuGroup}
DisableProgramGroupPage=Yes
LicenseFile={#ProjectPath}\LICENSE
; Uncomment the following line to run in non administrative install mode (install for current user only.)
; PrivilegesRequired=lowest
OutputDir={#ProjectPath}\inno-pyinstaller
OutputBaseFilename=full-installer
SetupIconFile={#ProjectPath}\myapplication\asset\cropped-cactus-512x512.ico
UninstallDisplayIcon={#ProjectPath}\myapplication\asset\cropped-cactus-512x512.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
WizardSmallImageFile={#ProjectPath}\myapplication\asset\small_installer_image_138x140.bmp
WizardImageFile={#ProjectPath}\myapplication\asset\big_installer_image_410x797.bmp

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
Name: "registerservice"; Description:"Register Service with OS"; GroupDescription:"Register Windows Service"; Components: service


[Files]
; Application Files
Source: "{#ProjectPath}\inno-pyinstaller\dist\MyApplication\{#MyAppExeName}"; DestDir: "{app}\{#AppDir}"; Flags: ignoreversion; Components: application
Source: "{#ProjectPath}\inno-pyinstaller\dist\MyApplication\*"; DestDir: "{app}\{#AppDir}"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: application
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
; Service Files
Source: "{#ProjectPath}\pyinstaller-service\dist\MyService\{#MySvcExeName}"; DestDir: "{app}\{#ServiceDir}"; Flags: ignoreversion; Components: service 
Source: "{#ProjectPath}\pyinstaller-service\dist\MyService\*"; DestDir: "{app}\{#ServiceDir}"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: service 


[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Components: application
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Tasks: desktopicon; Components: application
Name: "{group}\{#MySvcName} Configuration"; Filename: "{app}\{#ServiceDir}\{#MySvcExeName}"; Parameters: "--config-ui"; Components: service

[Run]
Filename: "{app}\{#AppDir}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent; Components: application
Filename: "{app}\{#ServiceDir}\{#MySvcExeName}"; Parameters: "--startup delayed install"; Description: "Register the Service"; Flags: runascurrentuser postinstall; Components: service; Tasks: registerservice;
;Filename: "{app}\{#ServiceDir}\{#MySvcExeName}"; Parameters: "start"; Description: "Start the Service"; Flags: runascurrentuser postinstall; Components: service; Tasks: registerservice;
; todo: start service

[UninstallRun]
Filename: "{app}\{#ServiceDir}\{#MySvcExeName}"; Parameters: "stop"; Components: service
Filename: "{app}\{#ServiceDir}\{#MySvcExeName}"; Parameters: "remove"; Components: service


; TODO start service make starting the service subbordinate to registring the service
; TODO Default to install for current user only (provide option to install for all users if it's trivial) Pending TS response




