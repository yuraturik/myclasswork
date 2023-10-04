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
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import time
# def countdown(user_time):
#     print("Starting countdown")
#     while user_time >= 0:
#         mins,secs = divmod(user_time,60)
#         timer = '{:02d}:{:02d}'.format(mins,secs)
#         print(timer,end='\r')
#         time.sleep(1)
#         user_time -= 1
#     print('Lift off')
# if __name__=='__main__':
#     user_time_1 = int(input("Enter a time in seconds:"))
#     countdown(user_time_1)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys
from PyQt6.QtWidgets import (QMainWindow,
QApplication,
QLabel,
QToolBar,
QStatusBar,
QCheckBox,
QSlider,
QGridLayout,
QWidget,
QDial)
from PyQt6.QtGui import QAction, QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Programka')




        toolbar = QToolBar('My main ToolBar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action4 = QAction('Файл', self)
        button_action4.setStatusTip('This is yout button')
        button_action4.triggered.connect(self.open_file_window)
        button_action4.setCheckable(True)
        toolbar.addAction(button_action4)

        button_action=QAction(QIcon('File_Explorer_23583.png'), 'Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('arrow_double_left_15739.png'), 'Your &button2', self)
        button_action2.setStatusTip('This is your button')
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        button_action5 = QAction(QIcon('PauseHot_26935.png'), 'Your &button2', self)
        button_action5.setStatusTip('This is your button')
        button_action5.triggered.connect(self.onMyToolBarButtonClick)
        button_action5.setCheckable(True)
        toolbar.addAction(button_action5)

        button_action3 = QAction(QIcon('arrow_double_right_15738.png'), 'Your &button2', self)
        button_action3.setStatusTip('This is your button')
        button_action3.triggered.connect(self.onMyToolBarButtonClick)
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)



        button_action6 = QAction('Редагування', self)
        button_action6.setStatusTip('This is yout button')
        button_action6.triggered.connect(self.onMyToolBarButtonClick)
        button_action6.setCheckable(True)
        toolbar.addAction(button_action6)

        button_action7 = QAction('Справка', self)
        button_action7.setStatusTip('This is yout button')
        button_action7.triggered.connect(self.open_info_window)
        button_action7.setCheckable(True)
        toolbar.addAction(button_action7)

        widget = QLabel()

        widget.setPixmap(QPixmap('Без названия.jpg'))
# widget.setFixedSize(700, 500)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        widget_1 = QLabel('One-Metallica')
        widget_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        widget_2 = QSlider()
        widget_2.setMaximum(10)
        widget_2.setMinimum(-10)
        widget_2 = QSlider(Qt.Orientation.Horizontal)

        widget_5 = QLabel(
        '0:00 2:55')
        widget_5.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        widget_3 = QDial()
        widget_3.setRange(1, 100)
        widget_3.setSingleStep(1)

        widget_4 = QSlider()
        widget_4.setMaximum(10)
        widget_4.setMinimum(-10)

        layout = QGridLayout()

        layout.addWidget(widget)
        layout.addWidget(widget_1 )
        layout.addWidget(widget_2)
        layout.addWidget(widget_5)
        layout.addWidget(widget_3, 4, 0)
        layout.addWidget(widget_4, 4,1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    def onMyToolBarButtonClick(self, s):
        print('click', s)


    def open_file_window(self):
        self.file_window = FileWindow()
        self.file_window.show()

    def open_info_window(self):
        self.info_window = InfoWindow()
        self.info_window.show()

class FileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File window")
        self.setGeometry(100, 100, 400, 200)

        label = QLabel('Здорова', self)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout2 = QGridLayout()
        layout2.addWidget(label, 2, 2)


class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info window")
        self.setGeometry(400, 400, 800, 600)

        label = QLabel('Info', self)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout = QGridLayout()
        layout.addWidget(label, 2, 2)



app = QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec()