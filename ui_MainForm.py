# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.wid_leInput = QtGui.QLineEdit(self.centralwidget)
        self.wid_leInput.setObjectName(_fromUtf8("wid_leInput"))
        self.verticalLayout_2.addWidget(self.wid_leInput)
        self.wid_lstWords = QtGui.QListWidget(self.centralwidget)
        self.wid_lstWords.setObjectName(_fromUtf8("wid_lstWords"))
        self.verticalLayout_2.addWidget(self.wid_lstWords)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wid_pleDis = QtGui.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wid_pleDis.setFont(font)
        self.wid_pleDis.setObjectName(_fromUtf8("wid_pleDis"))
        self.verticalLayout.addWidget(self.wid_pleDis)
        self.wid_lstKeywords = QtGui.QListWidget(self.centralwidget)
        self.wid_lstKeywords.setObjectName(_fromUtf8("wid_lstKeywords"))
        self.verticalLayout.addWidget(self.wid_lstKeywords)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.wid_leInput, self.wid_lstWords)
        MainWindow.setTabOrder(self.wid_lstWords, self.wid_lstKeywords)
        MainWindow.setTabOrder(self.wid_lstKeywords, self.wid_pleDis)
        MainWindow.setTabOrder(self.wid_pleDis, self.pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Grammar Glossary", None))
        self.pushButton.setText(_translate("MainWindow", "Quit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

