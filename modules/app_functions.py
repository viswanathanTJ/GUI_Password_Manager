
# ==> GUI FILE
from PySide2.QtCore import QTimer
from main import *
from modules.enc import *
from modules.dec import *
from modules.misc import *
from modules.app_modules import *
import sqlite3
import os
import pyperclip


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        print('createEditor event fired')
        return
    

createUser = ('''CREATE TABLE IF NOT EXISTS USER
    (USERNAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL,
    SHADOW TEXT NOT NULL);'''
    )
createManager = ('''CREATE TABLE IF NOT EXISTS MANAGER
    (DOMAIN TEXT NOT NULL,
    USERNAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL);'''    
    )

class Functions(MainWindow):
    signed = False
    
    # ==> FRESHUP FUNCTION
    ########################################################################
    def gotoHome(self):
        self.ui.label_top_info_1.setText('Password Manager')
        self.ui.label_top_info_2.setText('| Home')
        UIFunctions.resetStyle(self, "btn_home")
        UIFunctions.labelPage(self, "Home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        UIFunctions.addNewMenu(self, "Log Out", "btn_signout",
                               "url(:/16x16/icons/16x16/cil-exit-to-app.png)", False)
        self.ui.errorUpLabel.clear()
        self.ui.nameUpEntry.clear()
        self.ui.passUpEntry.clear()
        self.ui.passUpEntry2.clear()
        self.ui.nameInEntry.clear()
        self.ui.passInEntry.clear()
        self.ui.errorInLabel.clear()        
        self.ui.alertLabel.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        
    # ==> SIGN UP
    ########################################################################
    def signup(self):
        username = self.ui.nameUpEntry.text()
        password = self.ui.passUpEntry.text()
        password_2 = self.ui.passUpEntry2.text()
        if username and password and password_2 != '':
            if password == password_2:
                print(username, password, password_2)
                print('Signing Up...')
                if os.path.exists(username+'.db'):
                    print('[!!] User already exists')
                    self.ui.errorUpLabel.setText('[!!] Username already exists, Try Signing In')
                    self.ui.nameUpEntry.clear()
                else:
                    self.userid = username
                    user = sqlite3.connect(username+'.db')
                    cursor = user.cursor()
                    user.execute(createUser)
                    user.execute(createManager)
                    userHash = gen_sha3512_hash(username)
                    shadow = genShadow()
                    passShadow = password + shadow
                    passHash = gen_sha3512_hash(passShadow)
                    self.passDB = passHash
                    self.shadowDB = shadow
                    sql_user_adder = 'INSERT INTO USER (USERNAME,PASSWORD,SHADOW) VALUES (?,?,?)'
                    cursor.execute(sql_user_adder, (userHash, passHash,shadow,))
                    user.commit()
                    print('[+] New User Credentials Added :)\n')
                    print('Signed Up successfully')     
                    self.ui.errorInLabel.setText('Sign Up successful. Enter your cred to Sign In.')
                    self.ui.stackedWidget.setCurrentWidget(self.ui.signIn)   
            else:
                self.ui.errorUpLabel.setText('[!!] Passwords not matched')
                self.ui.passUpEntry.clear()
                self.ui.passUpEntry2.clear()
        else:
            self.ui.errorUpLabel.setText('[!!] Fill all fields')

    # ==> SIGN IN
    ########################################################################

    def signin(self):
        username = self.ui.nameInEntry.text()
        password = self.ui.passInEntry.text()
        if username and password != '':
            if os.path.exists(username+'.db'):
                print('Signing in...')
                user = sqlite3.connect(username+'.db')
                cursor = user.execute("SELECT PASSWORD, SHADOW from USER")
                data = cursor.fetchone()
                # print(data)
                self.passDB = data[0]
                self.shadowDB = data[1]
                passShadow = password + self.shadowDB
                passHash = gen_sha3512_hash(passShadow)
                if passHash == self.passDB:
                    self.signed = True
                    self.userid = username
                    Functions.gotoHome(self)
                    Functions.loadData(self)
                    print('==> Signin successful')                    
                    self.ui.alertLabel.setText('')
                else:
                    self.ui.errorInLabel.setText(
                        '[!!] Password does not match')
            else:
                self.ui.errorInLabel.setText('[!!] Username not found')
        else:
            self.ui.errorInLabel.setText(
                '[!!] Username and Password can not be null')

    # ==> ADD DATA TO TABLE
    ########################################################################

    def addtoTable(self):
        rowPosition = self.ui.tableWidget.rowCount()
        domain = self.ui.domainEntry.text()
        username = self.ui.usernameEntry.text()
        password = self.ui.passwordEntry.text()
        if domain and username and password != '':
            self.ui.domainEntry.clear()
            self.ui.usernameEntry.clear()
            self.ui.passwordEntry.clear()
            self.ui.tableWidget.insertRow(rowPosition)
            key = self.passDB
            username_enc = encryptor(username, key)
            password_enc = encryptor(password, key)
            Functions.addNewPassword(self, domain, username_enc, password_enc)
            self.ui.tableWidget.setItem(
                rowPosition, 0, QTableWidgetItem(domain))
            self.ui.tableWidget.setItem(
                rowPosition, 1, QTableWidgetItem(username))
            self.ui.tableWidget.setItem(
                rowPosition, 2, QTableWidgetItem(password))
            self.ui.alertLabel.setText('')
        else:
            self.ui.alertLabel.setText('[!!] Fill all data to save')

    # ==> LOAD DATA FROM TABLE
    ########################################################################

    def loadData(self):
        user = sqlite3.connect(self.userid+'.db')
        view_cursor = user.execute(
            "SELECT DOMAIN,USERNAME,PASSWORD from MANAGER")
        key = self.passDB
        for row in view_cursor:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            domain = row[0]
            username = decryptor(row[1], key)
            password = decryptor(row[2], key)
            self.ui.tableWidget.setItem(
                rowPosition, 0, QTableWidgetItem(domain))
            self.ui.tableWidget.setItem(
                rowPosition, 1, QTableWidgetItem(username))
            self.ui.tableWidget.setItem(
                rowPosition, 2, QTableWidgetItem(password))
        user.close()

    # ==> ADD DATA TO TABLE
    ########################################################################
    def addNewPassword(self, domain, username, password):
        user = sqlite3.connect(self.userid+'.db')
        cursor = user.cursor()
        sql_inserter = 'INSERT INTO MANAGER (DOMAIN,USERNAME, PASSWORD) VALUES (?,?,?)'
        cursor.execute(sql_inserter, (domain, username, password,))
        user.commit()
        # user.close()

    # ==> ROW MOVE
    ########################################################################
    def moveDown(self):
        row = self.ui.tableWidget.currentRow()
        column = self.ui.tableWidget.currentColumn()
        if row < self.ui.tableWidget.rowCount()-1:
            self.ui.tableWidget.insertRow(row+2)
            for i in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(
                    row+2, i, self.ui.tableWidget.takeItem(row, i))
                self.ui.tableWidget.setCurrentCell(row+2, column)
            self.ui.tableWidget.removeRow(row)

    def moveUp(self):
        row = self.ui.tableWidget.currentRow()
        column = self.ui.tableWidget.currentColumn()
        if row > 0 and self.ui.tableWidget.currentRow():
            self.ui.tableWidget.insertRow(row-1)
            for i in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(
                    row-1, i, self.ui.tableWidget.takeItem(row+1, i))
                self.ui.tableWidget.setCurrentCell(row-1, column)
            self.ui.tableWidget.removeRow(row+1)

    # ==> COPY PASSWORD
    ########################################################################
    def copyPass(self):
        row = self.ui.tableWidget.currentRow()
        password = self.ui.tableWidget.item(row, 2).text()
        domain = self.ui.tableWidget.item(row, 0).text()
        pyperclip.copy(password)
        self.ui.alertLabel.setText(
            f'[*] Password for {domain} copied successfully')

    # ==> DELETE ROW
    ########################################################################
    def deleteRow(self):
        row = self.ui.tableWidget.currentRow()
        domain = self.ui.tableWidget.item(row, 0).text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Warning! data can't be recovered")
        msg.setInformativeText("Confirm your action")
        msg.setWindowTitle("Alert")
        msg.setDetailedText(
            "Your data are stored as encrypted.\nIt is not possible to recover so beware in action.")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print("value of pressed message box button:", retval)
        if retval == 1024:
            print('Ok Pressed')
            user = sqlite3.connect(self.userid+'.db')
            user.execute("DELETE FROM MANAGER WHERE DOMAIN=?", (domain,))
            user.commit()
            self.ui.tableWidget.removeRow(row)
        else:
            print('Cancel Pressed')

    # ==> UPDATE ROW
    ########################################################################
    def updateRow(self):
        row = self.ui.tableWidget.currentRow()
        domain = self.ui.tableWidget.item(row, 0).text()
        password = self.ui.tableWidget.item(row, 2).text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Warning! old password can't be recovered")
        msg.setInformativeText("Confirm your action")
        msg.setWindowTitle("Alert")
        msg.setDetailedText(
            "Your data are stored as encrypted.\nIt is not possible to get old password so beware in action.")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == 1024:
            key = self.passDB
            password_enc = encryptor(password, key)
            user = sqlite3.connect(self.userid+'.db')
            user.execute(
                "UPDATE MANAGER SET PASSWORD=? WHERE DOMAIN=?", (password_enc, domain,))
            user.commit()
            print('[*] Updated successfully')            
            self.ui.alertLabel.setText('[*] Updated successfully')
        else:
            print('Cancel Pressed')

    # ==> SHOW HINT
    ########################################################################
    def showHint(self):
        self.ui.alertLabel.setText('Click update to save changed password')
    
    def removeLabel(self):
        self.ui.alertLabel.setText('')

    # ==> DELETE DB
    ########################################################################
    def delDB(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Warning! All your data will be completely wiped")
        msg.setInformativeText("Confirm your action")
        msg.setWindowTitle("Alert")
        msg.setDetailedText(
            "Your database will be completely wiped from the system!\nImpossible to recover")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == 1024:
            os.remove(self.userid+'.db')
            for item in self.ui.tableWidget.selectedItems():
                item.setText('')
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(3)
            self.ui.stackedWidget.setCurrentWidget(self.ui.signUp)
            self.ui.errorUpLabel.setText('[!!] Database deleted successfully')
        else:
            print('Cancel Pressed')