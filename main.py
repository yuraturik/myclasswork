# from PyQt6.QtWidgets import QApplication, QWidget
#
# # import sys
# # app = QApplication(sys.argv)
# app = QApplication([])
#
# window = QWidget()
# window.show()
#
# app.exec()

# from PyQt6.QtWidgets import QApplication, QPushButton
#
# app = QApplication([])
#
# obj_1 = QPushButton('PUSH')
# obj_1.show()
#
# app.exec()
# ----------------------------------------------------------------------------------------------
# from PyQt6.QtWidgets import QApplication, QMainWindow
#
# app = QApplication([])
#
# window = QMainWindow()
# window.show()
#
# app.exec()

# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt6.QtCore import QSize
#
# class MainWindow(QMainWindow):
#     def __int__(self):
#         super().__init__()
#
#         self.setWindowTitle('Перевірка імені')
#         button = QPushButton('Клікни')
#
#         self.setFixedSize(QSize(600,400))
#
#         self.setCentralWidget(button)
#
# app = QApplication([])
#
# window = MainWindow()
# window.show()
#
# app.exec()
# ------------------------------------------------------------------------------------------------------
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# a=0
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#
#
#         self.setWindowTitle('Moya programka')
#
#         button = QPushButton('click')
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_kliknuta)
#         button.clicked.connect(self.print_klik)
#         self.setCentralWidget(button)
#
#     def the_button_was_kliknuta(self):
#         print('Kliknuta!!!!!!!!!!!!!')
#
#     def print_klik(self):
#         global a
#         a+=1
#         print(a)
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
#---------------------------------------------------------------------------------------
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
# class MainWindow(QMainWindow):
#      def __init__(self):
#          super(MainWindow,self).__init__()
#          self.setWindowTitle('Moya programka')
#          button = QPushButton('click')
#          button.setCheckable(True)
#          button.clicked.connect(self.the_button_was_kliknuta)
#          button.clicked.connect(self.the_button_was_toggled)
#
#          self.setCentralWidget(button)
#
#      def the_button_was_kliknuta(self):
#          print('Kliknuta!!!!!!!!!!!!!')
#
#      def the_button_was_toggled(self,checked):
#         print('Checked?',checked)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
# -----------------------------------------------------
# import sys
# import time
#
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('Proga')
#         self.button = QPushButton('klikny')
#         self.button.clicked.connect(self.kliknuta_knopka)
#         self.setCentralWidget(self.button)
#
#     def kliknuta_knopka(self):
#         self.button.setText('Natysnuta')
#         self.button.setEnabled(False)
#         time.sleep(1)
#         self.button.setText('Ne natysnuta')
#         self.button.setEnabled(True)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
# -------------------------------------------------------------------
# QCheckBox - praporec
#QComboBox - spisok sho vupadae
#QDateEdit - redaguvanna datu
#QDateTimeEdit - redavuvana datu ta chasu
#QDial - kolesa slavik
#QFontComboBox - spisok shriftiv
#QDoubleSpinBox - redaguvanna cifr zavdaku strilochkam vgoru i vnuz
#QLCDNumber - display
#QLAbel - nadpis
#QLIneEdit - vod textu
#QProgresBar - indekator progresu
# QPushButton - knopka
# QRadioButton - radio knopka
# QSlider - povzunok
# QTimeEdit - redaguvanna chasu
# -----------------------------------------------------------------------
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import (QApplication,QCheckBox,QComboBox,QDateEdit,QDateTimeEdit,QDial,QDoubleSpinBox,QFontComboBox,
# QLabel,QLCDNumber,QLineEdit,QMainWindow,QProgressBar,QPushButton,QRadioButton,QSlider,QSpinBox,QTimeEdit,QVBoxLayout,QWidget)
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         self.setWindowTitle("Widgets")
#         layout = QVBoxLayout()
#         widgets = [QCheckBox,QComboBox,QDateEdit,QDateTimeEdit,QDial,QDoubleSpinBox,
#         QFontComboBox,QLabel,QLCDNumber,QLineEdit,
#         QProgressBar,QPushButton,QRadioButton,QSlider,
#         QSpinBox,QTimeEdit]
#         for i in widgets :
#             layout.addWidget(i())
#
#             widget = QWidget()
#             widget.setLayout(layout)
#             self.setCentralWidget(widget)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
#
# app.exec()
# ------------------------------------------------------------------------------
# QListWidget
# from PyQt6.QtWidgets import QListWidget,QComboBox,QMainWindow,QApplication,QWidget,QVBoxLayout
# from PyQt6.QtGui import QIcon
# import sys
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#
#         self.setWindowTitle('Proga')
#
#         input_1 = input(':')
#         input_2 = input(':')
#         input_3 =input(':')
#         input_4 = input(':')
#         input_5 = input(':')
#
#         widget = QListWidget()
#         widget.addItem(input_1)
#         widget.addItem(input_3)
#         widget.addItem(input_4)
#         widget.addItem(input_5)
#         widget.currentItemChanged.connect(self.index_changed)
#         widget.currentTextChanged.connect(self.text_changed)
#
#         widget.addItem(input_2)
#
#         self.setCentralWidget(widget)
#     def index_changed(self,i):
#         print(i.text())
#
#     def text_changed(self,s):
#         print(s)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
#
# app.exec()
# -------------------------------------------------------------------------------
# QLineEdit
# from PyQt6.QtWidgets import QLineEdit,QComboBox,QMainWindow,QApplication,QWidget,QVBoxLayout
# from PyQt6.QtGui import QIcon
# import sys
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#
#         self.setWindowTitle('QLineEdit')
#
#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText('enter your text')
#
#         widget.returnPressed.connect(self.return_presed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)
#
#         self.setCentralWidget(widget)
#
#     def return_presed(self):
#         print('Return pressed')
#         self.centralWidget().setText('Text!')
#     def selection_changed(self):
#         print('Selection changed')
#         print(self.centralWidget().selectedText())
#     def text_changed(self,s):
#         print('Changed')
#         print(s)
#     def text_edited(self,e):
#         print('Edited')
#         print(e)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
#
# app.exec()
import time
def countdown(user_time):
    print("Starting countdown")
    while user_time >= 0:
        mins,secs = divmod(user_time,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        user_time -= 1
    print('Lift off')
if __name__=='__main__':
    user_time_1 = int(input("Enter a time in seconds:"))
    countdown(user_time_1)