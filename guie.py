from PyQt5 import QtWidgets, uic
from encrypt import *
from zip import *
from psw import createpass
class Ui(QtWidgets.QMainWindow):
    createpass()
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('GUI.ui', self)
        self.input1 = self.findChild(QtWidgets.QLineEdit, 'Typepsw')
        self.input2 = self.findChild(QtWidgets.QLineEdit, 'Typepath')
        self.input3 = self.findChild(QtWidgets.QLineEdit, 'Value')
        self.radio1 = self.findChild(QtWidgets.QRadioButton, 'Manual')
        self.radio1 = self.findChild(QtWidgets.QRadioButton, 'Automatic')

        self.button1 = self.findChild(QtWidgets.QPushButton, 'Zip')
        self.button1.clicked.connect(self.WhenZipPressed)

        self.button2 = self.findChild(QtWidgets.QPushButton, 'Encrypt')
        if self.radio1.clicked:
            self.button2.clicked.connect(self.WhenEncryptPressed1)
        elif self.radio2.clicked:
            self.button2.clicked.connect(self.WhenEncryptPressed2)

        self.button3 = self.findChild(QtWidgets.QPushButton, 'Decrypt')
        if self.radio1.clicked:
            self.button3.clicked.connect(self.WhenDecryptPressed1)
        elif self.radio2.clicked:
            self.button3.clicked.connect(self.WhenDecryptPressed2)

        self.button4 = self.findChild(QtWidgets.QPushButton, 'Unzip')
        self.button1.clicked.connect(self.WhenUnzipPressed)
        self.show()

    def WhenZipPressed(self):
        a = self.input2.text()
        ZIP(a, a)

    def WhenEncryptPressed1(self):
        # This is executed when the button is pressed
        b = self.input1.text()
        a = self.input2.text()
        encrypt(getKey1(b, ), a)
        remove('psw.txt')

    def WhenEncryptPressed2(self):
        # This is executed when the button is pressed
        b = self.input1.text()
        a = self.input2.text()
        c =self.input3.text()
        encrypt(getKey2(b, c), a)
        remove('psw.txt')

    def WhenDecryptPressed1(self):
        # This is executed when the button is pressed
        b = self.input1.text()
        a = self.input2.text()
        decrypt(getKey1(b), a)
        remove('psw.txt')

    def WhenDecryptPressed2(self):
        # This is executed when the button is pressed
        b = self.input1.text()
        a = self.input2.text()
        c = self.input3.text()
        decrypt(getKey2(b, c), a)
        remove('psw.txt')
          
    def WhenUnzipPressed(self):
        a = self.input2.text()
        UNZIP(a)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gui = QtWidgets.QWidget()
    ui = Ui()

    sys.exit(app.exec_())
