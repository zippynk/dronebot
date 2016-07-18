#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Desktop/pbdronebot_tracker.ui'
#
# Created: Sun Jul 10 21:20:05 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost if you recompile the UI! But only if you recompile the UI! And there are tons of manual changes we made in here! SO DON'T YOU DARE RECOMPILE THE UI!

# This file ships with dronebot and is meant to be imported locally, not on the server.

#  (c) Copyright 2016 Nathan Krantz-Fire (a.k.a zippynk). Some rights reserved.
#  https://github.com/zippynk/dronebot

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from PySide import QtCore, QtGui
from image2 import *
from getloc2 import *
import urllib2
import json
import time

class Ui_pbdronebotTrackerWindow(object):
    def setupUi(self, pbdronebotTrackerWindow, server="localhost"):
        self.server = server
        pbdronebotTrackerWindow.setObjectName("pbdronebotTrackerWindow")
        pbdronebotTrackerWindow.resize(1440, 900)
        pbdronebotTrackerWindow.showFullScreen()
        self.mainWindow = pbdronebotTrackerWindow
        self.centralwidget = QtGui.QWidget(pbdronebotTrackerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        font.setPointSize(13)
        self.title.setObjectName("title")
        self.latstat = QtGui.QLabel(self.centralwidget)
        self.latstat.setGeometry(QtCore.QRect(10, 570, 121, 20))
        self.latstat.setFont(font)
        self.latstat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.latstat.setObjectName("latstat")
        self.lonstat = QtGui.QLabel(self.centralwidget)
        self.lonstat.setGeometry(QtCore.QRect(10, 590, 121, 20))
        self.lonstat.setFont(font)
        self.lonstat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lonstat.setObjectName("lonstat")
        self.locstat = QtGui.QLabel(self.centralwidget)
        self.locstat.setGeometry(QtCore.QRect(10, 610, 121, 20))
        self.locstat.setFont(font)
        self.locstat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.locstat.setObjectName("locstat")
        self.destinations = QtGui.QTableWidget(self.centralwidget)
        self.destinations.setGeometry(QtCore.QRect(10, 660, 681, pbdronebotTrackerWindow.height()-669))
        self.destinations.setObjectName("destinations")
        self.destinations.setColumnCount(4)
        self.destinations.setHorizontalHeaderLabels(["Latitude","Longitude","Action on Arrival","ETA"])
        self.lat = QtGui.QLabel(self.centralwidget)
        self.lat.setGeometry(QtCore.QRect(150, 570, 151, 20))
        self.lat.setFont(font)
        self.lat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lat.setObjectName("lat")
        self.lon = QtGui.QLabel(self.centralwidget)
        self.lon.setGeometry(QtCore.QRect(150, 590, 151, 20))
        self.lon.setFont(font)
        self.lon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lon.setObjectName("lon")
        self.loc = QtGui.QLabel(self.centralwidget)
        self.loc.setGeometry(QtCore.QRect(150, 610, 900, 20))
        self.loc.setFont(font)
        self.loc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.loc.setObjectName("loc")
        self.destinationsStat = QtGui.QLabel(self.centralwidget)
        self.destinationsStat.setGeometry(QtCore.QRect(10, 640, 101, 20))
        self.destinationsStat.setFont(font)
        self.destinationsStat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.destinationsStat.setObjectName("destinationsStat")
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(522, 51, 512, 512))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webView_2 = QtWebKit.QWebView(self.centralwidget)
        self.webView_2.setGeometry(QtCore.QRect(10, 50, 512, 512))
        self.webView_2.setUrl(QtCore.QUrl("about:blank"))
        self.webView_2.setObjectName("webView_2")
        pbdronebotTrackerWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(pbdronebotTrackerWindow)
        QtCore.QMetaObject.connectSlotsByName(pbdronebotTrackerWindow)
        self.mainThreadInstance = MainThread()
        self.mainThreadInstance.signal.sig.connect(self.update)
        self.mainThreadInstance.start()

    def retranslateUi(self, pbdronebotTrackerWindow):
        pbdronebotTrackerWindow.setWindowTitle(QtGui.QApplication.translate("pbdronebotTrackerWindow", "pbdronebot Tracker", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", "pbdronebot Tracker", None, QtGui.QApplication.UnicodeUTF8))
        self.latstat.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", "Latitude: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lonstat.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", "Longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.locstat.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", "Location Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.destinationsStat.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", "Destinations", None, QtGui.QApplication.UnicodeUTF8))
        #self.update()

    def update(self,data):
        data = json.loads(urllib2.urlopen("http://{0}:10407/update".format(self.server)).read())
        self.lat.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", str(data["lat"]), None, QtGui.QApplication.UnicodeUTF8))
        self.lon.setText(QtGui.QApplication.translate("pbdronebotTrackerWindow", str(data["lon"]), None, QtGui.QApplication.UnicodeUTF8))
        self.loc.setText(get_location(data["lat"],data["lon"]) if get_location(data["lat"],data["lon"]) != False else "Not Identified")
        url1 = world_map("zippynk.com",large=False)
        url2 = drone_close_up("zippynk.com",large=False)
        self.destinations.setRowCount(len(data["destinations"]))
        for i in range(len(data["destinations"])):
            self.destinations.setItem(i,0,QtGui.QTableWidgetItem(str(data["destinations"][i][0])))
            self.destinations.setItem(i,1,QtGui.QTableWidgetItem(str(data["destinations"][i][1])))
            self.destinations.setItem(i,2,QtGui.QTableWidgetItem("Dump" if data["destinations"][i][2] == True else "Continue" if data["destinations"][i][2] == False else "Data Error"))
            self.destinations.setItem(i,3,QtGui.QTableWidgetItem(str(data["destinations"][i][3])))
        self.destinations.resizeRowsToContents()
        self.destinations.resizeColumnsToContents()
        self.destinations.setGeometry(QtCore.QRect(10, 660, 681, self.mainWindow.height()-669))
        file1 = open("/tmp/img1.png","wb")
        file2 = open("/tmp/img2.png","wb")
        file1.write(urllib2.urlopen(url1).read())
        file2.write(urllib2.urlopen(url2).read())
        file1.close()
        file2.close()
        self.webView_2.load(QtCore.QUrl("file:///tmp/img1.png"))
        self.webView.load(QtCore.QUrl("file:///tmp/img2.png"))
        

class MainThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self,parent)
        self.exiting = False
        self.parent = parent
        self.signal = MySignal()
    def run(self):
        while True:
            data = json.loads(urllib2.urlopen("http://zippynk.com:10407/update").read())
            url1 = world_map("zippynk.com",large=False)
            url2 = drone_close_up("zippynk.com",large=False)
            file1 = open("/tmp/img1.png","wb")
            file2 = open("/tmp/img2.png","wb")
            file1.write(urllib2.urlopen(url1).read())
            file2.write(urllib2.urlopen(url2).read())
            file1.close()
            file2.close()
            self.signal.sig.emit(data)
            time.sleep(5)

class MySignal(QtCore.QObject):
        sig = QtCore.Signal(dict)

from PySide import QtWebKit
