from PySide6.QtWidgets import QApplication, QMainWindow

from ui.LoginMainWindowEx import LoginMainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()