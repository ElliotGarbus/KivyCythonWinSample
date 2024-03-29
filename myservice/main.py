# This file is for Secondary Objective #2
#
# Note: Need pip install pywin32


# Code is lifted from this blog post:
# https://metallapan.se/post/windows-service-pywin32-pyinstaller/

import sys
import time

import servicemanager  # Simple setup and logging
import win32service  # Events
import win32serviceutil  # ServiceFramework and commandline helper


sys.path.insert(0, "..")

from mylibrary import ProprietaryClass
from mylibrary.subdir import MyLib_Constants


class MyService:
    """Silly little application stub"""

    def stop(self):
        """Stop the service"""
        self.running = False

    def run(self):
        """Main service loop. This is where work is done!"""
        self.running = True
        secret = ProprietaryClass()
        while self.running:
            time.sleep(10)  # Important work
            secret_result = secret.hello_world()
            servicemanager.LogInfoMsg(f"{secret_result} {MyLib_Constants}")


class MyServiceFramework(win32serviceutil.ServiceFramework):
    _svc_name_ = 'MyService'
    _svc_display_name_ = 'My Service display name'

    def SvcStop(self):
        """Stop the service"""
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.service_impl.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        """Start the service; does not return until stopped"""
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.service_impl = MyService()
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        # Run the service
        self.service_impl.run()


def init():
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyServiceFramework)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyServiceFramework)


if __name__ == '__main__':
    init()
