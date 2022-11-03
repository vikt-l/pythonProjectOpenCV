# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 30, 521, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.video = QtWidgets.QLabel(self.frame)
        self.video.setGeometry(QtCore.QRect(30, 0, 481, 281))
        self.video.setObjectName("video")
        self.namesPeoples = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.namesPeoples.setGeometry(QtCore.QRect(40, 90, 341, 221))
        self.namesPeoples.setObjectName("namesPeoples")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 400, 171, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addPeople = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addPeople.setObjectName("addPeople")
        self.verticalLayout.addWidget(self.addPeople)
        self.btn_theme = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_theme.setText("")
        self.btn_theme.setObjectName("btn_theme")
        self.verticalLayout.addWidget(self.btn_theme)
        self.btn_help = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_theme.setText("help")
        self.btn_help.setObjectName("btn_help")
        self.verticalLayout.addWidget(self.btn_help)
        self.btnRecording = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRecording.setFont(font)
        self.btnRecording.setObjectName("btnRecording")
        self.verticalLayout.addWidget(self.btnRecording)
        self.btnStopRecording = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnStopRecording.setFont(font)
        self.btnStopRecording.setObjectName("btnStopRecording")
        self.verticalLayout.addWidget(self.btnStopRecording)
        self.lcdNumberPeople = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberPeople.setGeometry(QtCore.QRect(40, 60, 201, 23))
        self.lcdNumberPeople.setObjectName("lcdNumberPeople")
        self.lblNumberPeople = QtWidgets.QLabel(self.centralwidget)
        self.lblNumberPeople.setGeometry(QtCore.QRect(40, 30, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNumberPeople.setFont(font)
        self.lblNumberPeople.setObjectName("lblNumberPeople")
        self.infoPeople = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.infoPeople.setGeometry(QtCore.QRect(200, 370, 391, 201))
        self.infoPeople.setObjectName("infoPeople")
        self.dateTimeEd = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEd.setGeometry(QtCore.QRect(810, 370, 121, 22))
        self.dateTimeEd.setObjectName("dateTimeEd")
        self.lbl_date = QtWidgets.QLabel(self.centralwidget)
        self.lbl_date.setGeometry(QtCore.QRect(720, 370, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.cBoxNames = QtWidgets.QComboBox(self.centralwidget)
        self.cBoxNames.setGeometry(QtCore.QRect(40, 330, 251, 20))
        self.cBoxNames.setObjectName("cBoxNames")
        self.img_photo = QtWidgets.QLabel(self.centralwidget)
        self.img_photo.setGeometry(QtCore.QRect(40, 370, 141, 181))
        self.img_photo.setObjectName("img_photo")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(810, 410, 121, 23))
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.video.setText(_translate("MainWindow", "TextLabel"))
        self.addPeople.setText(_translate("MainWindow", "добавить в бд"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.btnRecording.setText(_translate("MainWindow", "запись видео"))
        self.btnStopRecording.setText(_translate("MainWindow", "остановить запись"))
        self.lblNumberPeople.setText(_translate("MainWindow", "количество человек на видео:"))
        self.lbl_date.setText(_translate("MainWindow", "дата и время"))
        self.img_photo.setText(_translate("MainWindow", "TextLabel"))
        self.start.setText(_translate("MainWindow", "start"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
