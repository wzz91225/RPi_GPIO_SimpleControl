# coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from ui_main import Ui_MainWindow

from GPIO_Control import GPIO_Control



class MainWindow(QMainWindow, Ui_MainWindow):
    DC_MIN = 0.0
    DC_MAX = 100.0
    FRE_MIN = 10
    FRE_MAX = 100
    
    dc = 50.0
    fre = 100
    
    gpio = None

    def __init__(self):
        self.window_init()
        self.gpio_init()
    
    def gpio_init(self):
        self.gpio = GPIO_Control([self.fre]*6, [self.dc]*6)
    
    def window_init(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("HelloWorld_PyQt5")

        # 占空比文本框
        validator_DC = QDoubleValidator(self)
        validator_DC.setRange(1, 100)
        validator_DC.setNotation(QDoubleValidator.StandardNotation)
        validator_DC.setDecimals(2)
        self.lineEdit_DC.setValidator(validator_DC)
        self.lineEdit_DC.setReadOnly(False)
        self.lineEdit_DC.editingFinished.connect(lambda: self.DC_Changed(self.lineEdit_DC))
        self.DC_DisplayUpdate()

        # 频率文本框
        validator_FRE = QIntValidator(self)
        validator_FRE.setRange(1, 100)
        self.lineEdit_FRE.setValidator(validator_FRE)
        self.lineEdit_FRE.setReadOnly(False)
        self.lineEdit_FRE.editingFinished.connect(lambda: self.FRE_Changed(self.lineEdit_FRE))
        self.FRE_DisplayUpdate()

        # 占空比增减按钮
        self.button_DC_UP.clicked.connect(lambda: self.Button_DC_UP())
        self.button_DC_DOWN.clicked.connect(lambda: self.Button_DC_DOWN())

        # 频率增减按钮
        self.button_FRE_UP.clicked.connect(lambda: self.Button_FRE_UP())
        self.button_FRE_DOWN.clicked.connect(lambda: self.Button_FRE_DOWN())


    def DC_Changed(self, lineEdit_DC):
        self.dc = float(lineEdit_DC.text())
        self.DC_OutputUpdate()
        self.DC_DisplayUpdate()

    def FRE_Changed(self, lineEdit_FRE):
        self.fre = int(lineEdit_FRE.text())
        self.FRE_OutputUpdate()
        self.FRE_DisplayUpdate()


    def DC_OutputUpdate(self):
        self.gpio.ChangeAllDutyCycle([self.dc]*6)

    def FRE_OutputUpdate(self):
        self.gpio.ChangeAllFrequency([self.fre]*6)


    def DC_DisplayUpdate(self):
        self.lineEdit_DC.setText(str(round(self.dc, 2)))

    def FRE_DisplayUpdate(self):
        self.lineEdit_FRE.setText(str(self.fre))


    def Button_DC_UP(self):
        self.dc += 1
        if self.dc > self.DC_MAX:
            self.dc = self.DC_MAX

        self.DC_OutputUpdate()
        self.DC_DisplayUpdate()

    def Button_DC_DOWN(self):
        self.dc -= 1
        if self.dc < self.DC_MIN:
            self.dc = self.DC_MIN

        self.DC_OutputUpdate()
        self.DC_DisplayUpdate()

    def Button_FRE_UP(self):
        self.fre += 1
        if self.fre > self.FRE_MAX:
            self.fre = self.FRE_MAX
        
        self.FRE_OutputUpdate()
        self.FRE_DisplayUpdate()

    def Button_FRE_DOWN(self):
        self.fre -= 1
        if self.fre < self.FRE_MIN:
            self.fre = self.FRE_MIN
        
        self.FRE_OutputUpdate()
        self.FRE_DisplayUpdate()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
