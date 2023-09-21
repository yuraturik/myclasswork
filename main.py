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