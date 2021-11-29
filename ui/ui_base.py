# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 685)
        MainWindow.setMinimumSize(QSize(810, 610))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.verticalLayout_18 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.signUp = QWidget()
        self.signUp.setObjectName(u"signUp")
        self.verticalLayout_10 = QVBoxLayout(self.signUp)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, -1, -1, -1)
        self.frame_head_content_2 = QFrame(self.signUp)
        self.frame_head_content_2.setObjectName(u"frame_head_content_2")
        self.frame_head_content_2.setMinimumSize(QSize(0, 110))
        self.frame_head_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_head_content_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_head_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_head_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_head_content_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.signInHeadLabel_2 = QLabel(self.frame_head_content_2)
        self.signInHeadLabel_2.setObjectName(u"signInHeadLabel_2")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(30)
        self.signInHeadLabel_2.setFont(font5)
        self.signInHeadLabel_2.setStyleSheet(u"QLabel{\n"
"	border:3px solid  rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(41, 45, 56);\n"
"}")
        self.signInHeadLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.signInHeadLabel_2)


        self.verticalLayout_10.addWidget(self.frame_head_content_2)

        self.login_form_frame_2 = QFrame(self.signUp)
        self.login_form_frame_2.setObjectName(u"login_form_frame_2")
        self.login_form_frame_2.setMinimumSize(QSize(450, 350))
        self.login_form_frame_2.setMaximumSize(QSize(500, 500))
        self.login_form_frame_2.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.login_form_frame_2.setFrameShape(QFrame.StyledPanel)
        self.login_form_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.login_form_frame_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 10, 3, 10)
        self.input_fileds_frame_3 = QFrame(self.login_form_frame_2)
        self.input_fileds_frame_3.setObjectName(u"input_fileds_frame_3")
        self.input_fileds_frame_3.setMaximumSize(QSize(500, 350))
        self.input_fileds_frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(34, 34, 34);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"}\n"
"QLineEdit {\n"
"	border: 2px solid rgb(0, 93, 159);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"	background-color: rgb(0, 69, 116);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(206, 206, 206);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"	background-color:rgb(14, 13, 24);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLabel{\n"
"	border:3px solid  rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(41, 45, 56);\n"
"}")
        self.input_fileds_frame_3.setFrameShape(QFrame.StyledPanel)
        self.input_fileds_frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.input_fileds_frame_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(6)
        self.icon_head_content_3 = QHBoxLayout()
        self.icon_head_content_3.setObjectName(u"icon_head_content_3")
        self.icon_head_content_3.setContentsMargins(-1, -1, 0, 10)
        self.verticalSpacer_5 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.icon_head_content_3.addItem(self.verticalSpacer_5)

        self.profile_icon_frame_3 = QFrame(self.input_fileds_frame_3)
        self.profile_icon_frame_3.setObjectName(u"profile_icon_frame_3")
        self.profile_icon_frame_3.setMinimumSize(QSize(50, 50))
        self.profile_icon_frame_3.setMaximumSize(QSize(50, 50))
        self.profile_icon_frame_3.setLayoutDirection(Qt.LeftToRight)
        self.profile_icon_frame_3.setStyleSheet(u"image: url(:/20x20/icons/20x20/cil-user.png);\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(0, 93, 159);")
        self.profile_icon_frame_3.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame_3.setFrameShadow(QFrame.Raised)

        self.icon_head_content_3.addWidget(self.profile_icon_frame_3)


        self.formLayout_4.setLayout(1, QFormLayout.SpanningRole, self.icon_head_content_3)

        self.usernameInLabel_3 = QLabel(self.input_fileds_frame_3)
        self.usernameInLabel_3.setObjectName(u"usernameInLabel_3")
        self.usernameInLabel_3.setMinimumSize(QSize(100, 50))
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.usernameInLabel_3.setFont(font6)
        self.usernameInLabel_3.setStyleSheet(u"")
        self.usernameInLabel_3.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.usernameInLabel_3)

        self.nameUpEntry = QLineEdit(self.input_fileds_frame_3)
        self.nameUpEntry.setObjectName(u"nameUpEntry")
        self.nameUpEntry.setMinimumSize(QSize(200, 50))
        self.nameUpEntry.setMaximumSize(QSize(200, 16777215))
        self.nameUpEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.nameUpEntry.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.nameUpEntry)

        self.passwordInLabel_3 = QLabel(self.input_fileds_frame_3)
        self.passwordInLabel_3.setObjectName(u"passwordInLabel_3")
        self.passwordInLabel_3.setMinimumSize(QSize(100, 50))
        self.passwordInLabel_3.setFont(font6)
        self.passwordInLabel_3.setStyleSheet(u"")
        self.passwordInLabel_3.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.passwordInLabel_3)

        self.passUpEntry = QLineEdit(self.input_fileds_frame_3)
        self.passUpEntry.setObjectName(u"passUpEntry")
        self.passUpEntry.setMinimumSize(QSize(200, 50))
        self.passUpEntry.setMaximumSize(QSize(200, 16777215))
        self.passUpEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.passUpEntry.setEchoMode(QLineEdit.Password)
        self.passUpEntry.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.passUpEntry)

        self.passwordInLabel_4 = QLabel(self.input_fileds_frame_3)
        self.passwordInLabel_4.setObjectName(u"passwordInLabel_4")
        self.passwordInLabel_4.setMinimumSize(QSize(100, 50))
        self.passwordInLabel_4.setFont(font6)
        self.passwordInLabel_4.setStyleSheet(u"")
        self.passwordInLabel_4.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.passwordInLabel_4)

        self.passUpEntry2 = QLineEdit(self.input_fileds_frame_3)
        self.passUpEntry2.setObjectName(u"passUpEntry2")
        self.passUpEntry2.setMinimumSize(QSize(200, 50))
        self.passUpEntry2.setMaximumSize(QSize(200, 16777215))
        self.passUpEntry2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.passUpEntry2.setEchoMode(QLineEdit.Password)
        self.passUpEntry2.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.passUpEntry2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.label_3 = QLabel(self.input_fileds_frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"border:none;\n"
"\n"
"	background-color: rgb(34, 34, 34);\n"
"}")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.gotoSign = QPushButton(self.input_fileds_frame_3)
        self.gotoSign.setObjectName(u"gotoSign")
        font7 = QFont()
        font7.setUnderline(True)
        self.gotoSign.setFont(font7)
        self.gotoSign.setCursor(QCursor(Qt.PointingHandCursor))
        self.gotoSign.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: rgb(34, 34, 34);\n"
"	padding:0px;\n"
"}")
        self.gotoSign.setAutoDefault(True)
        self.gotoSign.setFlat(False)

        self.gridLayout_4.addWidget(self.gotoSign, 0, 1, 1, 1)


        self.formLayout_4.setLayout(5, QFormLayout.FieldRole, self.gridLayout_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 5)
        self.regBtn = QPushButton(self.input_fileds_frame_3)
        self.regBtn.setObjectName(u"regBtn")
        self.regBtn.setMinimumSize(QSize(0, 50))
        self.regBtn.setMaximumSize(QSize(200, 16777215))
        self.regBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	outline: none;\n"
"}")
        self.regBtn.setAutoDefault(True)

        self.horizontalLayout_16.addWidget(self.regBtn)

        self.verticalSpacer_6 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_6)


        self.formLayout_4.setLayout(6, QFormLayout.SpanningRole, self.horizontalLayout_16)

        self.errorUpLabel = QLabel(self.input_fileds_frame_3)
        self.errorUpLabel.setObjectName(u"errorUpLabel")
        self.errorUpLabel.setFont(font6)
        self.errorUpLabel.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"border:none;")
        self.errorUpLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(7, QFormLayout.SpanningRole, self.errorUpLabel)


        self.verticalLayout_17.addWidget(self.input_fileds_frame_3, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.login_form_frame_2, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.signUp)
        self.signIn = QWidget()
        self.signIn.setObjectName(u"signIn")
        self.verticalLayout_13 = QVBoxLayout(self.signIn)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_head_content = QFrame(self.signIn)
        self.frame_head_content.setObjectName(u"frame_head_content")
        self.frame_head_content.setMinimumSize(QSize(0, 110))
        self.frame_head_content.setMaximumSize(QSize(16777215, 110))
        self.frame_head_content.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_head_content.setFrameShape(QFrame.NoFrame)
        self.frame_head_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_head_content)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.signInHeadLabel = QLabel(self.frame_head_content)
        self.signInHeadLabel.setObjectName(u"signInHeadLabel")
        self.signInHeadLabel.setFont(font5)
        self.signInHeadLabel.setStyleSheet(u"QLabel{\n"
"	border:3px solid  rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(41, 45, 56);\n"
"}")
        self.signInHeadLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.signInHeadLabel)


        self.verticalLayout_13.addWidget(self.frame_head_content)

        self.login_form_frame = QFrame(self.signIn)
        self.login_form_frame.setObjectName(u"login_form_frame")
        self.login_form_frame.setMinimumSize(QSize(450, 350))
        self.login_form_frame.setMaximumSize(QSize(500, 500))
        self.login_form_frame.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.login_form_frame.setFrameShape(QFrame.StyledPanel)
        self.login_form_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.login_form_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 10, 0, 10)
        self.input_fileds_frame = QFrame(self.login_form_frame)
        self.input_fileds_frame.setObjectName(u"input_fileds_frame")
        self.input_fileds_frame.setMaximumSize(QSize(500, 300))
        self.input_fileds_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(34, 34, 34);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"}\n"
"QLineEdit {\n"
"	border: 2px solid rgb(0, 93, 159);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"	background-color: rgb(0, 69, 116);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(206, 206, 206);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"	background-color:rgb(14, 13, 24);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLabel{\n"
"	border:3px solid  rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(41, 45, 56);\n"
"}")
        self.input_fileds_frame.setFrameShape(QFrame.StyledPanel)
        self.input_fileds_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.input_fileds_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.icon_head_content = QHBoxLayout()
        self.icon_head_content.setObjectName(u"icon_head_content")
        self.icon_head_content.setContentsMargins(-1, -1, 0, 10)
        self.verticalSpacer_2 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.icon_head_content.addItem(self.verticalSpacer_2)

        self.profile_icon_frame = QFrame(self.input_fileds_frame)
        self.profile_icon_frame.setObjectName(u"profile_icon_frame")
        self.profile_icon_frame.setMinimumSize(QSize(50, 50))
        self.profile_icon_frame.setMaximumSize(QSize(50, 50))
        self.profile_icon_frame.setLayoutDirection(Qt.LeftToRight)
        self.profile_icon_frame.setStyleSheet(u"image: url(:/20x20/icons/20x20/cil-user.png);\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(0, 93, 159);")
        self.profile_icon_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QFrame.Raised)

        self.icon_head_content.addWidget(self.profile_icon_frame)


        self.formLayout_2.setLayout(1, QFormLayout.SpanningRole, self.icon_head_content)

        self.usernameInLabel = QLabel(self.input_fileds_frame)
        self.usernameInLabel.setObjectName(u"usernameInLabel")
        self.usernameInLabel.setMinimumSize(QSize(100, 50))
        self.usernameInLabel.setFont(font6)
        self.usernameInLabel.setStyleSheet(u"")
        self.usernameInLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.usernameInLabel)

        self.nameInEntry = QLineEdit(self.input_fileds_frame)
        self.nameInEntry.setObjectName(u"nameInEntry")
        self.nameInEntry.setMinimumSize(QSize(200, 50))
        self.nameInEntry.setMaximumSize(QSize(200, 16777215))
        self.nameInEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.nameInEntry.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.nameInEntry)

        self.passwordInLabel = QLabel(self.input_fileds_frame)
        self.passwordInLabel.setObjectName(u"passwordInLabel")
        self.passwordInLabel.setMinimumSize(QSize(100, 50))
        self.passwordInLabel.setFont(font6)
        self.passwordInLabel.setStyleSheet(u"")
        self.passwordInLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.passwordInLabel)

        self.passInEntry = QLineEdit(self.input_fileds_frame)
        self.passInEntry.setObjectName(u"passInEntry")
        self.passInEntry.setMinimumSize(QSize(200, 50))
        self.passInEntry.setMaximumSize(QSize(200, 16777215))
        self.passInEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.passInEntry.setEchoMode(QLineEdit.Password)
        self.passInEntry.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.passInEntry)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.label = QLabel(self.input_fileds_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"border:none;\n"
"\n"
"	background-color: rgb(34, 34, 34);\n"
"}")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gotoReg = QPushButton(self.input_fileds_frame)
        self.gotoReg.setObjectName(u"gotoReg")
        self.gotoReg.setFont(font7)
        self.gotoReg.setCursor(QCursor(Qt.PointingHandCursor))
        self.gotoReg.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: rgb(34, 34, 34);\n"
"	padding:0px;\n"
"}")
        self.gotoReg.setFlat(True)

        self.gridLayout_2.addWidget(self.gotoReg, 0, 1, 1, 1)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.gridLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 5)
        self.loginBtn = QPushButton(self.input_fileds_frame)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 50))
        self.loginBtn.setMaximumSize(QSize(200, 16777215))
        self.loginBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	outline: 0 !important;\n"
"}")
        self.loginBtn.setAutoDefault(True)

        self.horizontalLayout_14.addWidget(self.loginBtn)

        self.verticalSpacer = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_14.addItem(self.verticalSpacer)


        self.formLayout_2.setLayout(5, QFormLayout.SpanningRole, self.horizontalLayout_14)

        self.errorInLabel = QLabel(self.input_fileds_frame)
        self.errorInLabel.setObjectName(u"errorInLabel")
        self.errorInLabel.setFont(font6)
        self.errorInLabel.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"border:none;")
        self.errorInLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.errorInLabel)


        self.verticalLayout_12.addWidget(self.input_fileds_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.login_form_frame, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.signIn)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_6 = QVBoxLayout(self.home_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.home_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxHint = QLabel(self.frame_title_wid_1)
        self.labelBoxHint.setObjectName(u"labelBoxHint")
        self.labelBoxHint.setFont(font1)
        self.labelBoxHint.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxHint)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.alertLabel = QLabel(self.frame_content_wid_1)
        self.alertLabel.setObjectName(u"alertLabel")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setWeight(75)
        self.alertLabel.setFont(font8)
        self.alertLabel.setStyleSheet(u"color: cyan;")
        self.alertLabel.setLineWidth(1)
        self.alertLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.alertLabel, 1, 0, 1, 6)

        self.domainEntry = QLineEdit(self.frame_content_wid_1)
        self.domainEntry.setObjectName(u"domainEntry")
        self.domainEntry.setMinimumSize(QSize(0, 40))
        self.domainEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.domainEntry.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.domainEntry, 0, 0, 1, 1)

        self.passwordEntry = QLineEdit(self.frame_content_wid_1)
        self.passwordEntry.setObjectName(u"passwordEntry")
        self.passwordEntry.setMinimumSize(QSize(0, 40))
        self.passwordEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.passwordEntry.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.passwordEntry, 0, 3, 1, 1)

        self.usernameEntry = QLineEdit(self.frame_content_wid_1)
        self.usernameEntry.setObjectName(u"usernameEntry")
        self.usernameEntry.setMinimumSize(QSize(0, 40))
        self.usernameEntry.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.usernameEntry.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.usernameEntry, 0, 1, 1, 1)

        self.addBtn = QPushButton(self.frame_content_wid_1)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(150, 40))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        self.addBtn.setFont(font9)
        self.addBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addBtn.setIcon(icon3)
        self.addBtn.setAutoDefault(True)

        self.gridLayout.addWidget(self.addBtn, 0, 4, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_3 = QFrame(self.home_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush12 = QBrush(QColor(39, 44, 54, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush12)
        brush13 = QBrush(QColor(52, 59, 72, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush13)
        self.tableWidget.setPalette(palette1)
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	alternate-background-color:rgb(52, 59, 72);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
""
                        "	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableCornerButton::section {\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"\n"
"}\n"
"QLineEdit {\n"
"	background: rgb(85, 170, 255);\n"
"	color:#000;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.home_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.moveUpBtn = QPushButton(self.frame_4)
        self.moveUpBtn.setObjectName(u"moveUpBtn")
        self.moveUpBtn.setMinimumSize(QSize(0, 40))
        self.moveUpBtn.setMaximumSize(QSize(50, 16777215))
        self.moveUpBtn.setFont(font9)
        self.moveUpBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-arrow-circle-top.png", QSize(), QIcon.Normal, QIcon.On)
        self.moveUpBtn.setIcon(icon4)
        self.moveUpBtn.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.moveUpBtn)

        self.moveDownBtn = QPushButton(self.frame_4)
        self.moveDownBtn.setObjectName(u"moveDownBtn")
        self.moveDownBtn.setMinimumSize(QSize(0, 40))
        self.moveDownBtn.setMaximumSize(QSize(50, 16777215))
        self.moveDownBtn.setFont(font9)
        self.moveDownBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-arrow-circle-bottom.png", QSize(), QIcon.Normal, QIcon.On)
        self.moveDownBtn.setIcon(icon5)
        self.moveDownBtn.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.moveDownBtn)

        self.copyBtn = QPushButton(self.frame_4)
        self.copyBtn.setObjectName(u"copyBtn")
        self.copyBtn.setMinimumSize(QSize(150, 40))
        self.copyBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/20x20/icons/20x20/cil-copy.png", QSize(), QIcon.Normal, QIcon.On)
        self.copyBtn.setIcon(icon6)
        self.copyBtn.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.copyBtn)

        self.updateBtn = QPushButton(self.frame_4)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setMinimumSize(QSize(150, 40))
        self.updateBtn.setFont(font9)
        self.updateBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateBtn.setIcon(icon7)
        self.updateBtn.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.updateBtn)

        self.deleteBtn = QPushButton(self.frame_4)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMinimumSize(QSize(150, 40))
        self.deleteBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.On)
        self.deleteBtn.setIcon(icon8)
        self.deleteBtn.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.deleteBtn)

        self.delDBBtn = QPushButton(self.frame_4)
        self.delDBBtn.setObjectName(u"delDBBtn")
        self.delDBBtn.setMinimumSize(QSize(0, 40))
        self.delDBBtn.setMaximumSize(QSize(50, 16777215))
        self.delDBBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(27, 29, 35);\n"
"	color: rgb(255, 255, 0)\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	background-color: rgb(57, 65, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/20x20/icons/20x20/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.On)
        self.delDBBtn.setIcon(icon9)

        self.horizontalLayout_11.addWidget(self.delDBBtn)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.home_page)

        self.verticalLayout_9.addWidget(self.stackedWidget, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        sizePolicy3.setHeightForWidth(self.label_credits.sizePolicy().hasHeightForWidth())
        self.label_credits.setSizePolicy(sizePolicy3)
        self.label_credits.setMinimumSize(QSize(0, 0))
        self.label_credits.setSizeIncrement(QSize(0, 0))
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.button_credits = QPushButton(self.frame_label_bottom)
        self.button_credits.setObjectName(u"button_credits")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.button_credits.sizePolicy().hasHeightForWidth())
        self.button_credits.setSizePolicy(sizePolicy5)
        self.button_credits.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_credits.setStyleSheet(u"color: rgb(98, 103, 111);\n"
"text-align:right;\n"
"border:none;")

        self.horizontalLayout_7.addWidget(self.button_credits)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_18.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.nameInEntry, self.passInEntry)
        QWidget.setTabOrder(self.passInEntry, self.loginBtn)
        QWidget.setTabOrder(self.loginBtn, self.gotoReg)
        QWidget.setTabOrder(self.gotoReg, self.nameUpEntry)
        QWidget.setTabOrder(self.nameUpEntry, self.passUpEntry)
        QWidget.setTabOrder(self.passUpEntry, self.passUpEntry2)
        QWidget.setTabOrder(self.passUpEntry2, self.regBtn)
        QWidget.setTabOrder(self.regBtn, self.gotoSign)
        QWidget.setTabOrder(self.gotoSign, self.domainEntry)
        QWidget.setTabOrder(self.domainEntry, self.usernameEntry)
        QWidget.setTabOrder(self.usernameEntry, self.passwordEntry)
        QWidget.setTabOrder(self.passwordEntry, self.addBtn)
        QWidget.setTabOrder(self.addBtn, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.moveUpBtn)
        QWidget.setTabOrder(self.moveUpBtn, self.moveDownBtn)
        QWidget.setTabOrder(self.moveDownBtn, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.copyBtn)
        QWidget.setTabOrder(self.copyBtn, self.updateBtn)
        QWidget.setTabOrder(self.updateBtn, self.deleteBtn)
        QWidget.setTabOrder(self.deleteBtn, self.btn_minimize)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.addBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"Crypto", None))
        self.signInHeadLabel_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.usernameInLabel_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.nameUpEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Username", None))
        self.passwordInLabel_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passUpEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.passwordInLabel_4.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.passUpEntry2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"             Already have an account?", None))
        self.gotoSign.setText(QCoreApplication.translate("MainWindow", u"SignIn", None))
        self.regBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.errorUpLabel.setText("")
        self.signInHeadLabel.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.usernameInLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.nameInEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Username", None))
        self.passwordInLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passInEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"          Don't have account?", None))
        self.gotoReg.setText(QCoreApplication.translate("MainWindow", u"Register Here", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.errorInLabel.setText("")
        self.labelBoxHint.setText(QCoreApplication.translate("MainWindow", u"ADD NEW", None))
        self.alertLabel.setText("")
        self.domainEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Domain/Url", None))
        self.passwordEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.usernameEntry.setText("")
        self.usernameEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.addBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Domain/Url", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username/Email", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.moveUpBtn.setText("")
        self.moveDownBtn.setText("")
        self.copyBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.delDBBtn.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By: Viswanathan TJ", None))
        self.button_credits.setText(QCoreApplication.translate("MainWindow", u"http://viswa2k.tk", None))
    # retranslateUi

