# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamesky_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 561, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_wp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.new_wp.setObjectName("new_wp")
        self.verticalLayout.addWidget(self.new_wp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_wp_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.new_wp_2.setObjectName("new_wp_2")
        self.horizontalLayout.addWidget(self.new_wp_2)
        self.wp_number = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.wp_number.setMinimum(1)
        self.wp_number.setMaximum(14)
        self.wp_number.setObjectName("wp_number")
        self.horizontalLayout.addWidget(self.wp_number)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startbt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startbt.setObjectName("startbt")
        self.horizontalLayout_2.addWidget(self.startbt)
        self.endbt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.endbt.setObjectName("endbt")
        self.horizontalLayout_2.addWidget(self.endbt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.download_edit = QtWidgets.QTextBrowser(self.centralwidget)
        self.download_edit.setGeometry(QtCore.QRect(0, 160, 561, 271))
        self.download_edit.setObjectName("download_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startbt.clicked.connect(MainWindow.DownloadEvent)
        self.endbt.clicked.connect(MainWindow.StopEvent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_wp.setText(_translate("MainWindow", "最新的一期："))
        self.new_wp_2.setText(_translate("MainWindow", "需要下载的期数："))
        self.startbt.setText(_translate("MainWindow", "开始下载"))
        self.endbt.setText(_translate("MainWindow", "停止下载"))

