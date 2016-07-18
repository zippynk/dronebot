#!/usr/bin/env python2

# This file ships with dronebot and is meant to be run locally, not on the server.

#  (c) Copyright 2016 Nathan Krantz-Fire (a.k.a zippynk). Some rights reserved.
#  https://github.com/zippynk/dronebot

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pbdronebot_tracker_ui import *
import sys

if len(sys.argv) < 2:
    print("Usage: python pbdronebot_tracker.py [server]")

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_pbdronebotTrackerWindow()
        self.ui.setupUi(self,server=sys.argv[1])
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
