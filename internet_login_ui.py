# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Desktop/InternetLogin.ui'
#
# Created: Sun Jul 31 20:04:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_InternetLoginWindow(object):
    def setupUi(self, InternetLoginWindow):
        InternetLoginWindow.setObjectName("InternetLoginWindow")
        InternetLoginWindow.resize(560, 480)
        self.buttonBox = QtGui.QDialogButtonBox(InternetLoginWindow)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 536, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.webView = QtWebKit.QWebView(InternetLoginWindow)
        self.webView.setGeometry(QtCore.QRect(10, 30, 536, 400))
        self.webView.setUrl(QtCore.QUrl("http://web.archive.org/web/20160418120732/https://upload.wikimedia.org/wikipedia/commons/b/bc/PeanutButter.jpg"))
        self.webView.setObjectName("webView")
        self.label = QtGui.QLabel(InternetLoginWindow)
        self.label.setGeometry(QtCore.QRect(10, 5, 341, 21))
        self.label.setObjectName("label")

        self.retranslateUi(InternetLoginWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), InternetLoginWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), InternetLoginWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(InternetLoginWindow)

    def retranslateUi(self, InternetLoginWindow):
        InternetLoginWindow.setWindowTitle(QtGui.QApplication.translate("InternetLoginWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InternetLoginWindow", "Internet Login", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
