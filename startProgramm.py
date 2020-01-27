from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from sys import argv, exit
from interface.mainPage import Main_page
from interface.loginPage import Login_page
from interface.inc import Pass_inc_page
from interface.addUser import AddUserI
from interface.removeUser import RemoveUserI
from interface.camera import Camera
from interface.sql import select_user_sql, add_user_sql, remove_user_sql
from interface.video import Ui_MainWindow as video
from video_stream import process_video_stream



class Video(video, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_10.clicked.connect(self.openFileNameDialog)
        self.pushButton_11.clicked.connect(self.start)

    def start(self):
        self.hide()
        process_video_stream(self.lineEdit.text())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*);;Png (*.png);;Jpg (*.jpg)", options=options)
        if fileName:
            self.lineEdit.setText(fileName)
        else:
            self.lineEdit.setText('Path Error')


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
        self.pushButton_7.clicked.connect(self.stream)
        self.addUser = AddUserPage(self)
        self.removeUser = RemoveUserPage(self)
        self.video = Video(self)
        self.pushButton_6.clicked.connect(self.exit)
        self.ipCamera = IpCamera(self)
        self.pushButton_2.clicked.connect(self.videoStart)
        self.pushButton_3.clicked.connect(self.videoStart)

    def videoStart(self):
        self.video.show()

    def stream(self):
        process_video_stream()

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
        # temp = select_user_sql(self.lineEdit.text())
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'admin':
            self.main_page = Main_pages(self)
            self.main_page.show()
            self.hide()
        else:
            self.passInc.show()


def main():
    app = QApplication(argv)
    ex = Login_page()
    ex.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
