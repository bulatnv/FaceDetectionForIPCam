from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from sys import argv, exit
from mainPage import Main_page
from loginPage import Login_page
from inc import Pass_inc_page
from addUser import AddUserI
from removeUser import RemoveUserI
from camera import Camera
from sql import select_user_sql, add_user_sql, remove_user_sql


class IpCamera(Camera, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)

    def hide(self):
        self.hide()


class AddUserPage(AddUserI, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.openFileNameDialog)

    def add(self):
        if self.lineEdit_2 != '' and self.lineEdit != '':
            add_user_sql(self.lineEdit_2.text(), self.lineEdit.text())
        self.hide()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*);;Png (*.png);;Jpg (*.jpg)", options=options)
        if fileName:
            self.lineEdit.setText(fileName)
        else:
            self.lineEdit.setText('Path Error')


class RemoveUserPage(RemoveUserI, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.remove)

    def remove(self):
        if self.lineEdit_2.text() != '':
            remove_user_sql(self.lineEdit_2.text())
        self.hide()


class Main_pages(Main_page, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.add_user)
        self.pushButton_5.clicked.connect(self.remove_user)
        self.pushButton.clicked.connect(self.ip_camera)
        self.addUser = AddUserPage(self)
        self.removeUser = RemoveUserPage(self)
        self.pushButton_6.clicked.connect(self.exit)
        self.ipCamera = IpCamera(self)

    def ip_camera(self):
        self.ipCamera.show()
        pass

    def add_user(self):
        self.addUser.show()

    def remove_user(self):
        self.removeUser.show()

    def exit(self):
        self.close()


class Pass_inc(Pass_inc_page, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inc)

    def inc(self):
        self.hide()


class Login_page(Login_page, QMainWindow):
    def __init__(self):
        super().__init__()
        self.passInc = Pass_inc(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        temp = select_user_sql(self.lineEdit.text())
        if temp == []:
            self.passInc.show()
        elif self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'admin':
            self.main_page = Main_pages(self)
            self.main_page.show()
            self.hide()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Login_page()
    ex.show()
    exit(app.exec())
