# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created: Mon Nov  7 20:16:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 354)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.left = QtGui.QGridLayout()
        self.left.setObjectName("left")
        self.lOffen = QtGui.QLabel(self.centralwidget)
        self.lOffen.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOffen.sizePolicy().hasHeightForWidth())
        self.lOffen.setSizePolicy(sizePolicy)
        self.lOffen.setScaledContents(False)
        self.lOffen.setObjectName("lOffen")
        self.left.addWidget(self.lOffen, 0, 1, 1, 1)
        self.lFalsch = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFalsch.sizePolicy().hasHeightForWidth())
        self.lFalsch.setSizePolicy(sizePolicy)
        self.lFalsch.setObjectName("lFalsch")
        self.left.addWidget(self.lFalsch, 2, 1, 1, 1)
        self.lGesamt = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lGesamt.sizePolicy().hasHeightForWidth())
        self.lGesamt.setSizePolicy(sizePolicy)
        self.lGesamt.setObjectName("lGesamt")
        self.left.addWidget(self.lGesamt, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.left.addWidget(self.label_2, 0, 0, 1, 1)
        self.lKorrekt = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lKorrekt.sizePolicy().hasHeightForWidth())
        self.lKorrekt.setSizePolicy(sizePolicy)
        self.lKorrekt.setObjectName("lKorrekt")
        self.left.addWidget(self.lKorrekt, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.left.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.left.addWidget(self.label_7, 3, 0, 1, 1)
        self.lSpiele = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSpiele.sizePolicy().hasHeightForWidth())
        self.lSpiele.setSizePolicy(sizePolicy)
        self.lSpiele.setObjectName("lSpiele")
        self.left.addWidget(self.lSpiele, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.left.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.left.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.left, 0, 0, 3, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.b9 = QtGui.QPushButton(self.centralwidget)
        self.b9.setObjectName("b9")
        self.gridLayout_2.addWidget(self.b9, 1, 0, 1, 1)
        self.b4 = QtGui.QPushButton(self.centralwidget)
        self.b4.setObjectName("b4")
        self.gridLayout_2.addWidget(self.b4, 1, 1, 1, 1)
        self.b6 = QtGui.QPushButton(self.centralwidget)
        self.b6.setObjectName("b6")
        self.gridLayout_2.addWidget(self.b6, 2, 1, 1, 1)
        self.b7 = QtGui.QPushButton(self.centralwidget)
        self.b7.setObjectName("b7")
        self.gridLayout_2.addWidget(self.b7, 0, 1, 1, 1)
        self.b14 = QtGui.QPushButton(self.centralwidget)
        self.b14.setObjectName("b14")
        self.gridLayout_2.addWidget(self.b14, 0, 2, 1, 1)
        self.b8 = QtGui.QPushButton(self.centralwidget)
        self.b8.setObjectName("b8")
        self.gridLayout_2.addWidget(self.b8, 1, 2, 1, 1)
        self.b10 = QtGui.QPushButton(self.centralwidget)
        self.b10.setObjectName("b10")
        self.gridLayout_2.addWidget(self.b10, 1, 4, 1, 1)
        self.b5 = QtGui.QPushButton(self.centralwidget)
        self.b5.setObjectName("b5")
        self.gridLayout_2.addWidget(self.b5, 0, 3, 1, 1)
        self.b2 = QtGui.QPushButton(self.centralwidget)
        self.b2.setObjectName("b2")
        self.gridLayout_2.addWidget(self.b2, 0, 4, 1, 1)
        self.b12 = QtGui.QPushButton(self.centralwidget)
        self.b12.setObjectName("b12")
        self.gridLayout_2.addWidget(self.b12, 2, 0, 1, 1)
        self.b11 = QtGui.QPushButton(self.centralwidget)
        self.b11.setObjectName("b11")
        self.gridLayout_2.addWidget(self.b11, 2, 4, 1, 1)
        self.b1 = QtGui.QPushButton(self.centralwidget)
        self.b1.setObjectName("b1")
        self.gridLayout_2.addWidget(self.b1, 0, 0, 1, 1)
        self.b0 = QtGui.QPushButton(self.centralwidget)
        self.b0.setObjectName("b0")
        self.gridLayout_2.addWidget(self.b0, 1, 3, 1, 1)
        self.b13 = QtGui.QPushButton(self.centralwidget)
        self.b13.setObjectName("b13")
        self.gridLayout_2.addWidget(self.b13, 2, 2, 1, 1)
        self.b3 = QtGui.QPushButton(self.centralwidget)
        self.b3.setObjectName("b3")
        self.gridLayout_2.addWidget(self.b3, 2, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Moonbeam")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bNeu = QtGui.QPushButton(self.centralwidget)
        self.bNeu.setObjectName("bNeu")
        self.horizontalLayout_3.addWidget(self.bNeu)
        self.bEnde = QtGui.QPushButton(self.centralwidget)
        self.bEnde.setObjectName("bEnde")
        self.horizontalLayout_3.addWidget(self.bEnde)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_2.setBuddy(self.label_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lOffen.setText(QtGui.QApplication.translate("MainWindow", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.lFalsch.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lGesamt.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Offen:", None, QtGui.QApplication.UnicodeUTF8))
        self.lKorrekt.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Spiele:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Gesamt:", None, QtGui.QApplication.UnicodeUTF8))
        self.lSpiele.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Falsch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Korrekt:", None, QtGui.QApplication.UnicodeUTF8))
        self.b9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.b4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.b6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.b7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.b14.setText(QtGui.QApplication.translate("MainWindow", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.b8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.b10.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.b5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.b2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.b12.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.b11.setText(QtGui.QApplication.translate("MainWindow", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.b1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.b0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.b13.setText(QtGui.QApplication.translate("MainWindow", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.b3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Klicken Sie die Buttons in aufsteigender Reihenfolge!", None, QtGui.QApplication.UnicodeUTF8))
        self.bNeu.setText(QtGui.QApplication.translate("MainWindow", "Neu", None, QtGui.QApplication.UnicodeUTF8))
        self.bEnde.setText(QtGui.QApplication.translate("MainWindow", "Ende", None, QtGui.QApplication.UnicodeUTF8))
