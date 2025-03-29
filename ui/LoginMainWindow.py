# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginMainWindowACXbWS.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1370, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u";\n"
"background-color: rgb(221, 221, 221);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 30, 941, 611))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.label.setPixmap(QPixmap(u"../images/login 2.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 110, 471, 71))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font: 45pt \".VnBodoni\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditUserName = QLineEdit(self.centralwidget)
        self.lineEditUserName.setObjectName(u"lineEditUserName")
        self.lineEditUserName.setGeometry(QRect(540, 290, 301, 31))
        sizePolicy.setHeightForWidth(self.lineEditUserName.sizePolicy().hasHeightForWidth())
        self.lineEditUserName.setSizePolicy(sizePolicy)
        self.lineEditUserName.setStyleSheet(u"QlineEdit{\n"
" font: 16pt \"MS Shell Dlg 2\";\n"
" border:2px solid rgb(38,38,48);\n"
" border-radius: 15px;\n"
" color:#FFF;\n"
" background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(38,38,48);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
" boder:2px soild rgb(35,218,233);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.pushButtonLogin = QPushButton(self.centralwidget)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setGeometry(QRect(540, 470, 311, 41))
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        self.pushButtonLogin.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(39, 19, 11);\n"
"  boder-radius:15px;\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  font: 18pt \".VnBodoni\";\n"
"	\n"
"  \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgba(0, 0, 0, 150);\n"
"  font: 18pt \".VnBodoni\";\n"
" }\n"
"")
        icon = QIcon()
        icon.addFile(u"../icon/icon_login.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonLogin.setIcon(icon)
        self.pushButtonLogin.setIconSize(QSize(35, 35))
        self.pushButtonExit = QPushButton(self.centralwidget)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        self.pushButtonExit.setGeometry(QRect(540, 520, 311, 41))
        sizePolicy.setHeightForWidth(self.pushButtonExit.sizePolicy().hasHeightForWidth())
        self.pushButtonExit.setSizePolicy(sizePolicy)
        self.pushButtonExit.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(39, 19, 11);\n"
"  boder-radius:15px;\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  font: 18pt \".VnBodoni\";\n"
"	\n"
"  \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgba(0, 0, 0, 150);\n"
"  font: 18pt \".VnBodoni\";\n"
" }\n"
"QPushButton {\n"
"	background-color: rgb(39, 19, 11);\n"
"  boder-radius:15px;\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  font: 18pt \".VnBodoni\";\n"
"	\n"
"  \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgba(0, 0, 0, 150);\n"
"  font: 18pt \".VnBodoni\";\n"
" }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../icon/icon_logout.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonExit.setIcon(icon1)
        self.pushButtonExit.setIconSize(QSize(35, 35))
        self.radioButtonForget = QRadioButton(self.centralwidget)
        self.radioButtonForget.setObjectName(u"radioButtonForget")
        self.radioButtonForget.setGeometry(QRect(690, 380, 141, 31))
        sizePolicy.setHeightForWidth(self.radioButtonForget.sizePolicy().hasHeightForWidth())
        self.radioButtonForget.setSizePolicy(sizePolicy)
        self.radioButtonForget.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.lineEditPassWord = QLineEdit(self.centralwidget)
        self.lineEditPassWord.setObjectName(u"lineEditPassWord")
        self.lineEditPassWord.setGeometry(QRect(540, 340, 301, 31))
        sizePolicy.setHeightForWidth(self.lineEditPassWord.sizePolicy().hasHeightForWidth())
        self.lineEditPassWord.setSizePolicy(sizePolicy)
        self.lineEditPassWord.setStyleSheet(u"QlineEdit{\n"
" border:2px solid rgb(38,38,48);\n"
" border-radius: 15px;\n"
" color:#FFF;\n"
" background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(38,38,48);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
" boder:2px soild rgb(35,218,233);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.lineEditPassWord.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditPassWord.setClearButtonEnabled(False)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 200, 471, 51))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font: 45pt \".VnBodoni\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_QuanLyDangNhap = QPushButton(self.centralwidget)
        self.pushButton_QuanLyDangNhap.setObjectName(u"pushButton_QuanLyDangNhap")
        self.pushButton_QuanLyDangNhap.setGeometry(QRect(580, 420, 221, 24))
        self.pushButton_QuanLyDangNhap.setStyleSheet(u"QPushButton {\n"
"		border:  none;\n"
"		background-color: rgb(43, 35, 31);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	text-decoration: underline;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1370, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>COFFEE</p></body></html>", None))
        self.lineEditUserName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.radioButtonForget.setText(QCoreApplication.translate("MainWindow", u"Forget Password", None))
        self.lineEditPassWord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"BUSINESS", None))
        self.pushButton_QuanLyDangNhap.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp t\u01b0 c\u00e1ch l\u00e0 qu\u1ea3n l\u00fd", None))
    # retranslateUi

