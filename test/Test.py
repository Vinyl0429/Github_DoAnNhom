from PySide6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowExt import MainWindowExt

app = QApplication([])

mainwindow = QMainWindow()
ui = MainWindowExt()
ui.setupUi(mainwindow)
ui.show_window()

app.exec()
