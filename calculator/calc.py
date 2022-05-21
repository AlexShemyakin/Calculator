from PyQt5.QtWidgets import *
from operator import add, sub, mul, truediv
from calc_form import Ui_Form

operations = {
    '+': add,
    '-': sub,
    '/': truediv,
    '*': mul
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.count = 0
        self.temp = ''
        self.temp_2 = ''
        self.sign = ''


        self.ui.pushButton_n1.pressed.connect(self.add_digit)
        self.ui.pushButton_n2.pressed.connect(self.add_digit)
        self.ui.pushButton_n3.pressed.connect(self.add_digit)
        self.ui.pushButton_n4.pressed.connect(self.add_digit)
        self.ui.pushButton_n5.pressed.connect(self.add_digit)
        self.ui.pushButton_n6.pressed.connect(self.add_digit)
        self.ui.pushButton_n7.pressed.connect(self.add_digit)
        self.ui.pushButton_n8.pressed.connect(self.add_digit)
        self.ui.pushButton_n9.pressed.connect(self.add_digit)
        self.ui.pushButton_n0.pressed.connect(self.add_digit)
        self.ui.pushButton_ac.pressed.connect(self.clear)
        self.ui.pushButton_sub.pressed.connect(self.math_operation)
        self.ui.pushButton_add.pressed.connect(self.math_operation)
        self.ui.pushButton_div.pressed.connect(self.math_operation)
        self.ui.pushButton_multi.pressed.connect(self.math_operation)
        self.ui.pushButton_summ.pressed.connect(self.math_operation)


    def add_digit(self):
        btn = self.sender()

        digit_buttons = ('pushButton_n0', 'pushButton_n1', 'pushButton_n2', 'pushButton_n3', 'pushButton_n4',
                         'pushButton_n5', 'pushButton_n6', 'pushButton_n7', 'pushButton_n8', 'pushButton_n9')


        if self.ui.textBrowser.toPlainText() == '0':
            self.ui.textBrowser.setText(btn.text())
            self.add_temp(btn.text())
        else:
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + btn.text())
            self.add_temp(btn.text())


    def add_temp(self, temp):
        if self.count == 1:
            self.temp += temp
        else:
            self.temp_2 += temp


    def math_operation(self):
        btn = self.sender()
        self.count += 1
        if self.count == 1:
            self.sign = btn.text()
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + f' {btn.text()} ')
        else:
            try:
                result = operations[self.sign](int(self.temp_2), int(self.temp))
            except ZeroDivisionError:
                result = 'Деление на ноль'
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + f' {btn.text()} ' + f'{result}')
            self.count = 0
            self.temp = ''
            self.temp_2 = ''
            self.sign = ''


    def clear(self):
        self.ui.textBrowser.setText('0')
        self.count = 0
        self.temp = ''
        self.temp_2 = ''
        self.sign = ''


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = MainWindow()
    window.show()
    app.exec_()
