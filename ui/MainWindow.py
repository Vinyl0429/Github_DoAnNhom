# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowItPoie.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget, QGridLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 574)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toggle.sizePolicy().hasHeightForWidth())
        self.frame_toggle.setSizePolicy(sizePolicy)
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(118, 62, 50);")
        self.frame_toggle.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy1)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u"../icon/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Btn_Toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_top.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_left_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButtonpageOder = QPushButton(self.frame_top_menus)
        self.pushButtonpageOder.setObjectName(u"pushButtonpageOder")
        self.pushButtonpageOder.setMinimumSize(QSize(0, 40))
        self.pushButtonpageOder.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Arial\";\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../images/4908132_chef_food_hotel_platter_service_icon (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonpageOder.setIcon(icon1)
        self.pushButtonpageOder.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButtonpageOder)

        self.pushButtonpageProduct = QPushButton(self.frame_top_menus)
        self.pushButtonpageProduct.setObjectName(u"pushButtonpageProduct")
        self.pushButtonpageProduct.setMinimumSize(QSize(0, 40))
        self.pushButtonpageProduct.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../images/889384_barista_black coffee_coffee_cup_cup of coffee_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonpageProduct.setIcon(icon2)
        self.pushButtonpageProduct.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButtonpageProduct)

        self.pushButtonpageEmployee = QPushButton(self.frame_top_menus)
        self.pushButtonpageEmployee.setObjectName(u"pushButtonpageEmployee")
        self.pushButtonpageEmployee.setMinimumSize(QSize(0, 40))
        self.pushButtonpageEmployee.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../icon/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonpageEmployee.setIcon(icon3)
        self.pushButtonpageEmployee.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButtonpageEmployee)

        self.pushButtonpageChamCong = QPushButton(self.frame_top_menus)
        self.pushButtonpageChamCong.setObjectName(u"pushButtonpageChamCong")
        self.pushButtonpageChamCong.setMinimumSize(QSize(0, 40))
        self.pushButtonpageChamCong.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../images/2203551_book_calendar_date_monthly_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonpageChamCong.setIcon(icon4)
        self.pushButtonpageChamCong.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButtonpageChamCong)

        self.pushButtonpageStatistics = QPushButton(self.frame_top_menus)
        self.pushButtonpageStatistics.setObjectName(u"pushButtonpageStatistics")
        self.pushButtonpageStatistics.setMinimumSize(QSize(0, 40))
        self.pushButtonpageStatistics.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../images/103716_statistics_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonpageStatistics.setIcon(icon5)
        self.pushButtonpageStatistics.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButtonpageStatistics)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_pages.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.pageProduct = QWidget()
        self.pageProduct.setObjectName(u"pageProduct")
        self.horizontalLayout_8 = QHBoxLayout(self.pageProduct)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_3 = QGroupBox(self.pageProduct)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet(u"font: 700 15pt \"Arial\";\n"
"color: rgb(118, 62, 50);")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea = QScrollArea(self.groupBox_3)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 436, 452))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.pageProduct)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"../images/5402443_search_find_magnifier_magnifying_magnifying glass_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.lineEditSearch = QLineEdit(self.frame)
        self.lineEditSearch.setObjectName(u"lineEditSearch")
        sizePolicy1.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy1)
        self.lineEditSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";")

        self.horizontalLayout_3.addWidget(self.lineEditSearch)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_12.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.groupBox = QGroupBox(self.pageProduct)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
"color: rgb(118, 62, 50);")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.label_2)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.label_8)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.label_7)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.label_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lineEditID = QLineEdit(self.groupBox)
        self.lineEditID.setObjectName(u"lineEditID")
        self.lineEditID.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.lineEditID)

        self.lineEditName = QLineEdit(self.groupBox)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.lineEditName)

        self.lineEditCategory = QLineEdit(self.groupBox)
        self.lineEditCategory.setObjectName(u"lineEditCategory")
        self.lineEditCategory.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.lineEditCategory)

        self.lineEditQuantity = QLineEdit(self.groupBox)
        self.lineEditQuantity.setObjectName(u"lineEditQuantity")
        self.lineEditQuantity.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.lineEditQuantity)

        self.lineEditPrice = QLineEdit(self.groupBox)
        self.lineEditPrice.setObjectName(u"lineEditPrice")
        self.lineEditPrice.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.lineEditPrice)


        self.horizontalLayout_4.addLayout(self.verticalLayout_17)


        self.verticalLayout_12.addWidget(self.groupBox)

        self.frame_2 = QFrame(self.pageProduct)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
"color: rgb(118, 62, 50);")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonNew = QPushButton(self.groupBox_2)
        self.pushButtonNew.setObjectName(u"pushButtonNew")
        sizePolicy3.setHeightForWidth(self.pushButtonNew.sizePolicy().hasHeightForWidth())
        self.pushButtonNew.setSizePolicy(sizePolicy3)
        self.pushButtonNew.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 62, 50);")

        self.horizontalLayout_5.addWidget(self.pushButtonNew)

        self.pushButtonSave = QPushButton(self.groupBox_2)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        sizePolicy3.setHeightForWidth(self.pushButtonSave.sizePolicy().hasHeightForWidth())
        self.pushButtonSave.setSizePolicy(sizePolicy3)
        self.pushButtonSave.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 62, 50);")

        self.horizontalLayout_5.addWidget(self.pushButtonSave)

        self.pushButtonDelete = QPushButton(self.groupBox_2)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        sizePolicy3.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy3)
        self.pushButtonDelete.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 62, 50);")

        self.horizontalLayout_5.addWidget(self.pushButtonDelete)


        self.verticalLayout_13.addWidget(self.groupBox_2, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.pageProduct)
        self.pageOrder = QWidget()
        self.pageOrder.setObjectName(u"pageOrder")
        self.horizontalLayout_9 = QHBoxLayout(self.pageOrder)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayoutSearch = QHBoxLayout()
        self.horizontalLayoutSearch.setObjectName(u"horizontalLayoutSearch")
        self.label_4 = QLabel(self.pageOrder)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(118, 62, 50);\n"
"font: 700 16pt \"Segoe UI\";")

        self.horizontalLayoutSearch.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_7 = QFrame(self.pageOrder)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.horizontalLayoutSearch.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_10.addLayout(self.horizontalLayoutSearch)

        self.horizontalLayoutFilterMenu = QHBoxLayout()
        self.horizontalLayoutFilterMenu.setObjectName(u"horizontalLayoutFilterMenu")

        self.verticalLayout_10.addLayout(self.horizontalLayoutFilterMenu)

        self.horizontalLayoutBriefInformation = QHBoxLayout()
        self.horizontalLayoutBriefInformation.setObjectName(u"horizontalLayoutBriefInformation")
        self.horizontalLayoutBriefInformation.setContentsMargins(15, 10, -1, 0)
        self.label_10 = QLabel(self.pageOrder)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setStyleSheet(u"color: rgb(118, 62, 50);\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayoutBriefInformation.addWidget(self.label_10)

        self.label_5 = QLabel(self.pageOrder)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setStyleSheet(u"color: rgb(118, 62, 50);\n"
"font: 700 16pt \"Segoe UI\";")

        self.horizontalLayoutBriefInformation.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.horizontalLayoutBriefInformation)

        self.groupBoxMenu = QGroupBox(self.pageOrder)
        self.groupBoxMenu.setObjectName(u"groupBoxMenu")
        sizePolicy1.setHeightForWidth(self.groupBoxMenu.sizePolicy().hasHeightForWidth())
        self.groupBoxMenu.setSizePolicy(sizePolicy1)
        self.groupBoxMenu.setStyleSheet(u"QGroupBox { border: none; }\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.groupBoxMenu)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollAreaProductMenu = QScrollArea(self.groupBoxMenu)
        self.scrollAreaProductMenu.setObjectName(u"scrollAreaProductMenu")
        self.scrollAreaProductMenu.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 504, 387))
        self.scrollAreaProductMenu.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollAreaProductMenu.setWidget(self.scrollAreaWidgetContents_2)

        # Đổi từ QVBoxLayout sang QGridLayout
        self.gridLayout_ProductMenu = QGridLayout(self.scrollAreaWidgetContents_2)
        self.scrollAreaWidgetContents_2.setLayout(self.gridLayout_ProductMenu)


        self.verticalLayout_19.addWidget(self.scrollAreaProductMenu)


        self.verticalLayout_10.addWidget(self.groupBoxMenu)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_5 = QFrame(self.pageOrder)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setMaximumSize(QSize(16000, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEditCustomerName = QLineEdit(self.frame_6)
        self.lineEditCustomerName.setObjectName(u"lineEditCustomerName")
        self.lineEditCustomerName.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.lineEditCustomerName)

        self.lineEditCustomerPhoneNumber = QLineEdit(self.frame_6)
        self.lineEditCustomerPhoneNumber.setObjectName(u"lineEditCustomerPhoneNumber")
        self.lineEditCustomerPhoneNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.lineEditCustomerPhoneNumber)

        self.pushButtonDiscount = QPushButton(self.frame_6)
        self.pushButtonDiscount.setObjectName(u"pushButtonDiscount")
        self.pushButtonDiscount.setStyleSheet(u"background-color: rgb(118, 62, 50);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.pushButtonDiscount)


        self.horizontalLayout_10.addWidget(self.frame_6)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.orderWidget = QWidget(self.frame_5)
        self.orderWidget.setObjectName(u"orderWidget")
        sizePolicy1.setHeightForWidth(self.orderWidget.sizePolicy().hasHeightForWidth())
        self.orderWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_23 = QVBoxLayout(self.orderWidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_Order = QVBoxLayout()
        self.verticalLayout_Order.setObjectName(u"verticalLayout_Order")

        self.verticalLayout_23.addLayout(self.verticalLayout_Order)


        self.verticalLayout_20.addWidget(self.orderWidget)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.pushButton_printBill = QPushButton(self.frame_5)
        self.pushButton_printBill.setObjectName(u"pushButton_printBill")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_printBill.sizePolicy().hasHeightForWidth())
        self.pushButton_printBill.setSizePolicy(sizePolicy6)
        self.pushButton_printBill.setStyleSheet(u"background-color: rgb(118, 62, 50);\n"
"color: rgb(255, 255, 255);\n"
"font: 600 14pt \"Segoe UI\";\n"
"\n"
"")

        self.verticalLayout_21.addWidget(self.pushButton_printBill)


        self.verticalLayout_18.addWidget(self.frame_5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_18)

        self.stackedWidget.addWidget(self.pageOrder)
        self.pageChamCong = QWidget()
        self.pageChamCong.setObjectName(u"pageChamCong")
        self.verticalLayout_28 = QVBoxLayout(self.pageChamCong)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton = QPushButton(self.pageChamCong)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_18.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.pageChamCong)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(22, 99, 17);")

        self.horizontalLayout_18.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.pageChamCong)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 210, 97);")

        self.horizontalLayout_18.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.pageChamCong)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_18.addWidget(self.pushButton_4)


        self.verticalLayout_28.addLayout(self.horizontalLayout_18)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_3 = QWidget(self.pageChamCong)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy7)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_30 = QVBoxLayout(self.widget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_26.addWidget(self.label_13)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_26.addWidget(self.label_12)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_26.addWidget(self.label_11)


        self.horizontalLayout_19.addLayout(self.verticalLayout_26)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lineEdit_2 = QLineEdit(self.widget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy8)

        self.verticalLayout_32.addWidget(self.lineEdit_2)

        self.comboBox_3 = QComboBox(self.widget_4)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy9)

        self.verticalLayout_32.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox(self.widget_4)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy9.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy9)

        self.verticalLayout_32.addWidget(self.comboBox_2)


        self.horizontalLayout_19.addLayout(self.verticalLayout_32)


        self.verticalLayout_30.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.verticalLayout_33 = QVBoxLayout(self.widget_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.pushButtonLoadChamCong = QPushButton(self.widget_5)
        self.pushButtonLoadChamCong.setObjectName(u"pushButtonLoadChamCong")

        self.verticalLayout_33.addWidget(self.pushButtonLoadChamCong, 0, Qt.AlignmentFlag.AlignTop)

        self.pushButtonSave_Check = QPushButton(self.widget_5)
        self.pushButtonSave_Check.setObjectName(u"pushButtonSave_Check")

        self.verticalLayout_33.addWidget(self.pushButtonSave_Check)


        self.verticalLayout_30.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_17.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tableWidgetChamCong = QTableWidget(self.widget_3)
        self.tableWidgetChamCong.setObjectName(u"tableWidgetChamCong")
        sizePolicy.setHeightForWidth(self.tableWidgetChamCong.sizePolicy().hasHeightForWidth())
        self.tableWidgetChamCong.setSizePolicy(sizePolicy)

        self.verticalLayout_31.addWidget(self.tableWidgetChamCong)


        self.horizontalLayout_17.addLayout(self.verticalLayout_31)


        self.verticalLayout_27.addWidget(self.widget_3)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)

        self.stackedWidget.addWidget(self.pageChamCong)
        self.pageStatistics = QWidget()
        self.pageStatistics.setObjectName(u"pageStatistics")
        self.verticalLayout_25 = QVBoxLayout(self.pageStatistics)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget1 = QWidget(self.pageStatistics)
        self.widget1.setObjectName(u"widget1")
        sizePolicy3.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy3)
        self.widget1.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_12 = QHBoxLayout(self.widget1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frameCustomer = QFrame(self.widget1)
        self.frameCustomer.setObjectName(u"frameCustomer")
        sizePolicy3.setHeightForWidth(self.frameCustomer.sizePolicy().hasHeightForWidth())
        self.frameCustomer.setSizePolicy(sizePolicy3)
        self.frameCustomer.setMaximumSize(QSize(16777215, 150))
        self.frameCustomer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCustomer.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frameCustomer)

        self.frameRevenue = QFrame(self.widget1)
        self.frameRevenue.setObjectName(u"frameRevenue")
        sizePolicy3.setHeightForWidth(self.frameRevenue.sizePolicy().hasHeightForWidth())
        self.frameRevenue.setSizePolicy(sizePolicy3)
        self.frameRevenue.setMaximumSize(QSize(16777215, 150))
        self.frameRevenue.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRevenue.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frameRevenue)

        self.frameInvoices = QFrame(self.widget1)
        self.frameInvoices.setObjectName(u"frameInvoices")
        sizePolicy3.setHeightForWidth(self.frameInvoices.sizePolicy().hasHeightForWidth())
        self.frameInvoices.setSizePolicy(sizePolicy3)
        self.frameInvoices.setMaximumSize(QSize(16777215, 150))
        self.frameInvoices.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameInvoices.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frameInvoices)


        self.verticalLayout_22.addWidget(self.widget1)


        self.verticalLayout_25.addLayout(self.verticalLayout_22)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_2 = QWidget(self.pageStatistics)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16775))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_bieudo = QFrame(self.widget_2)
        self.frame_bieudo.setObjectName(u"frame_bieudo")
        sizePolicy.setHeightForWidth(self.frame_bieudo.sizePolicy().hasHeightForWidth())
        self.frame_bieudo.setSizePolicy(sizePolicy)
        self.frame_bieudo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bieudo.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.frame_bieudo)

        self.frame_bieudo1 = QFrame(self.widget_2)
        self.frame_bieudo1.setObjectName(u"frame_bieudo1")
        sizePolicy.setHeightForWidth(self.frame_bieudo1.sizePolicy().hasHeightForWidth())
        self.frame_bieudo1.setSizePolicy(sizePolicy)
        self.frame_bieudo1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bieudo1.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.frame_bieudo1)


        self.verticalLayout_24.addWidget(self.widget_2)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)

        self.stackedWidget.addWidget(self.pageStatistics)
        self.pageEmployee = QWidget()
        self.pageEmployee.setObjectName(u"pageEmployee")
        self.verticalLayout_9 = QVBoxLayout(self.pageEmployee)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.pageEmployee)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_4 = QGroupBox(self.frame_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.pushButton_6)

        self.lineEditSearchEmployee = QLineEdit(self.groupBox_4)
        self.lineEditSearchEmployee.setObjectName(u"lineEditSearchEmployee")

        self.horizontalLayout_15.addWidget(self.lineEditSearchEmployee)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButtonDetails_E = QPushButton(self.groupBox_4)
        self.pushButtonDetails_E.setObjectName(u"pushButtonDetails_E")
        self.pushButtonDetails_E.setStyleSheet(u"background-color: rgb(118, 62, 50);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.pushButtonDetails_E)

        self.pushButtonDeleteEmployee = QPushButton(self.groupBox_4)
        self.pushButtonDeleteEmployee.setObjectName(u"pushButtonDeleteEmployee")
        self.pushButtonDeleteEmployee.setStyleSheet(u"background-color: rgb(118, 62, 50);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.pushButtonDeleteEmployee)

        self.pushButtonAddEmployee = QPushButton(self.groupBox_4)
        self.pushButtonAddEmployee.setObjectName(u"pushButtonAddEmployee")
        self.pushButtonAddEmployee.setStyleSheet(u"background-color: rgb(118, 62, 50);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.pushButtonAddEmployee)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_6.addWidget(self.groupBox_4)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.pageEmployee)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tableWidgetEmployee = QTableWidget(self.frame_3)
        if (self.tableWidgetEmployee.columnCount() < 6):
            self.tableWidgetEmployee.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetEmployee.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetEmployee.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetEmployee.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetEmployee.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetEmployee.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetEmployee.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidgetEmployee.setObjectName(u"tableWidgetEmployee")

        self.verticalLayout_14.addWidget(self.tableWidgetEmployee)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.pageEmployee)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Coffee Management", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButtonpageOder.setText("")
        self.pushButtonpageProduct.setText("")
        self.pushButtonpageEmployee.setText("")
        self.pushButtonpageChamCong.setText("")
        self.pushButtonpageStatistics.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"List of products", None))
        self.pushButton_5.setText("")
        self.lineEditSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search somthing here", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Product Details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Quantity:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButtonNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Choose Category", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Coffee Menu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBoxMenu.setTitle("")
        self.lineEditCustomerName.setText("")
        self.lineEditCustomerName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer's name", None))
        self.lineEditCustomerPhoneNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.pushButtonDiscount.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.pushButton_printBill.setText(QCoreApplication.translate("MainWindow", u"Print bill", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng c\u00f3 l\u1ecbch", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0110i l\u00e0m", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ngh\u1ec9 c\u00f3 ph\u00e9p", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Ngh\u1ec9 kh\u00f4ng ph\u00e9p", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"N\u0103m", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Th\u00e1ng", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tu\u1ea7n", None))
        self.pushButtonLoadChamCong.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButtonSave_Check.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"List of Employee", None))
        self.pushButton_6.setText("")
        self.pushButtonDetails_E.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.pushButtonDeleteEmployee.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButtonAddEmployee.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.tableWidgetEmployee.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidgetEmployee.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidgetEmployee.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None));
        ___qtablewidgetitem3 = self.tableWidgetEmployee.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Phone number", None));
        ___qtablewidgetitem4 = self.tableWidgetEmployee.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem5 = self.tableWidgetEmployee.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Start_working_date", None));
    # retranslateUi

