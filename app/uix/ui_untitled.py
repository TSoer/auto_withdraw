# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledJZkmIh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient, QAction)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 643)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txtBrowserLog = QTextBrowser(self.centralwidget)
        self.txtBrowserLog.setObjectName(u"txtBrowserLog")

        self.gridLayout.addWidget(self.txtBrowserLog, 2, 0, 1, 2)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.gridLayout.addWidget(self.btnStart, 1, 0, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430 \u0441 \u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0430\u043c\u0438", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0430\u0440\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0444\u0430\u0439\u043b \u0441 \u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0430\u043c\u0438", None))
    # retranslateUi

