import sys
import webbrowser
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import modules.app_modules_mongo
# GUI FILE
from modules.app_modules_mongo import *


## ==> GLOBALS
counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # START - WINDOW ATTRIBUTES
        ########################################################################

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        # SET ==> WINDOW TITLE
        self.setWindowTitle('Crypto - MongoDB')
        UIFunctions.labelTitle(self, 'Crypto - MongoDB')
        UIFunctions.labelDescription(self, 'Home Page')
        ## ==> END ##

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(800, 620)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        # ==> CREATE MENUS
        ########################################################################

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Add User", "btn_new_user",
                               "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "HOME", "btn_home",
                               "url(:/16x16/icons/16x16/cil-home.png)", True)
        # UIFunctions.addNewMenu(self, "Custom Widgets", "btn_signout", "url(:/16x16/icons/16x16/cil-cil-exit-to-app.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_new_user")
        ## ==> END ##

        # ==> START PAGE        
        self.ui.stackedWidget.setCurrentWidget(self.ui.signUp)
        self.ui.label_top_info_1.setText('Registration')
        self.ui.label_top_info_2.setText('| Form')

        ## ==> END ##

        # ==> FORM PAGE
        self.ui.gotoReg.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget
                                        (self.ui.signUp))
        self.ui.gotoSign.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget
                                         (self.ui.signIn))
        ## ==> END ##

        # USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "Crypto", "", True)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## START -------------- BUTTON CLICK FUCNCTION -----------------------##
        #                                                                      #
        ##                                                                    ##
        ########################################################################
        self.ui.addBtn.clicked.connect(lambda: Mongo.addtoTable(self))
        self.ui.loginBtn.clicked.connect(lambda: Mongo.signin(self))
        self.ui.regBtn.clicked.connect(lambda: Mongo.signup(self))
        self.ui.moveUpBtn.clicked.connect(lambda: Mongo.moveUp(self))
        self.ui.moveDownBtn.clicked.connect(lambda: Mongo.moveDown(self))
        self.ui.deleteBtn.clicked.connect(lambda: Mongo.deleteRow(self))
        self.ui.copyBtn.clicked.connect(lambda: Mongo.copyPass(self))
        self.ui.updateBtn.clicked.connect(lambda: Mongo.updateRow(self))
        self.ui.delDBBtn.clicked.connect(lambda: Mongo.delDB(self))
        self.ui.button_credits.clicked.connect(lambda: webbrowser.open('http://viswa2k.tk'))
        self.ui.tableWidget.doubleClicked.connect(lambda: Mongo.showHint(self))
        self.ui.tableWidget.clicked.connect(lambda: Mongo.removeLabel(self))

        # ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        # ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        # END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        # ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        delegate = ReadOnlyDelegate(self)
        self.ui.tableWidget.setItemDelegateForColumn(0, delegate)
        self.ui.tableWidget.setItemDelegateForColumn(1, delegate)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    # MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))
            if Mongo.signed == False:
                self.ui.alertLabel.setText('[!!] Login to see data')
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(3)

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.signUp)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_signout":
            self.ui.stackedWidget.setCurrentWidget(self.ui.signIn)
            UIFunctions.resetStyle(self, "btn_signout")
            UIFunctions.labelPage(self, "Welcome")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))
            for item in self.ui.tableWidget.selectedItems():
                item.setText('')
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(3)
            btnWidget.deleteLater()

    ## ==> END ##

    ########################################################################
    # START ==> APP EVENTS
    ########################################################################

    # EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            # print('Mouse click: LEFT CLICK')
            self.ui.alertLabel.setText('')
            self.ui.errorInLabel.setText('')
            self.ui.errorUpLabel.setText('')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')
        # if event.buttons() == Qt.MidButton:
        #     print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    # EVENT ==> RESIZE EVENT
    ########################################################################

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) +
              ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    # END ==> APP EVENTS
    ############################## ---/--/--- ##############################

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(25)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>STRONG</strong> ENCRYPTIONS")
        # Change Texts
        QtCore.QTimer.singleShot(2500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1
 
class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        print('createEditor event fired')
        return
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = SplashScreen()
    sys.exit(app.exec_())