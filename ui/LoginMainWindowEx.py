from PySide6.QtWidgets import (
    QLineEdit, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QLabel, QDialog, QSizePolicy, QSpacerItem
)
from models.DataConnector import DataConnector
from models.PopupBox import PopupBox
from ui.LoginMainWindow import Ui_MainWindow
from ui.MainWindowExt import MainWindowExt

class LoginMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

        self.setLineEditStyle(self.lineEditUserName, focus=False)
        self.setLineEditStyle(self.lineEditPassWord, focus=False)

        self.lineEditUserName.focusInEvent = lambda event: self.setLineEditStyle(self.lineEditUserName, focus=True)
        self.lineEditUserName.focusOutEvent = lambda event: self.setLineEditStyle(self.lineEditUserName, focus=False)
        self.lineEditPassWord.focusInEvent = lambda event: self.setLineEditStyle(self.lineEditPassWord, focus=True)
        self.lineEditPassWord.focusOutEvent = lambda event: self.setLineEditStyle(self.lineEditPassWord, focus=False)

        self.popup  = PopupBox()
        self.dc  = DataConnector()
        self.pushButton_QuanLyDangNhap.setCheckable(True)


    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButton_QuanLyDangNhap.clicked.connect(self.process_login)
        self.radioButtonForget.toggled.connect(self.show_password_reset)
        self.lineEditUserName.returnPressed.connect(self.lineEditPassWord.setFocus)
        self.lineEditPassWord.returnPressed.connect(self.process_login)

    def showWindow(self):
        self.MainWindow.show()

    def process_login(self):
        """ Xử lý đăng nhập với quyền nhân viên hoặc quản lý """
        dc = DataConnector()
        is_manager = False  # Mặc định là nhân viên

        # 👉 Kiểm tra nếu nhấn "Đăng nhập với tư cách quản lý"
        if self.pushButton_QuanLyDangNhap.isChecked():
            uid = self.lineEditUserName.text().strip()
            pwd = self.lineEditPassWord.text().strip()

            # ❌ Nếu chưa nhập đủ thông tin → Hiện cảnh báo
            if not uid or not pwd:
                self.popup.show_warning("⚠ Vui lòng nhập tài khoản và mật khẩu để đăng nhập với tư cách quản lý!")
                return

            # 👉 Kiểm tra tài khoản
            emp = dc.login(uid, pwd)
            if emp is None:
                self.popup.show_warning("❌ Sai tài khoản hoặc mật khẩu! Vui lòng thử lại.")
                return  # ❌ Dừng lại, không cho vào hệ thống

            is_manager = True  # ✅ Đăng nhập thành công với vai trò Quản lý

        print(f"🛠 DEBUG: is_manager = {is_manager}")  # 👀 Kiểm tra quyền

        # 👉 Mở giao diện chính
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = MainWindowExt()
        self.myui.setupUi(self.mainwindow)

        # 🚀 Cập nhật quyền truy cập
        print(f"🔹 Gọi set_permissions với quyền: {'Quản lý' if is_manager else 'Nhân viên'}")
        self.set_permissions(is_manager)

        self.myui.show_window()

    def set_permissions(self, is_manager):
        """ Cấu hình quyền truy cập dựa trên vai trò """
        if not hasattr(self, 'myui') or self.myui is None:
            print("LỖI: Giao diện chưa được khởi tạo!")
            return

        # Nếu là quản lý, mở tất cả các nút
        self.myui.pushButtonpageProduct.setEnabled(is_manager)
        self.myui.pushButtonpageOder.setEnabled(True)  # Order luôn mở
        self.myui.pushButtonpageStatistics.setEnabled(is_manager)
        self.myui.pushButtonpageEmployee.setEnabled(is_manager)
        self.myui.pushButtonpageChamCong.setEnabled(is_manager)

        print(f"🔹 Quyền truy cập đã được cập nhật: {'Quản lý' if is_manager else 'Nhân viên'}")

    def show_password_reset(self, checked):
        if checked:
            dialog = PasswordResetDialog(self.MainWindow)
            dialog.exec()

    def setLineEditStyle(self, line_edit: QLineEdit, focus: bool):
        if focus:
            line_edit.setStyleSheet("""
                QLineEdit {
                    border: 2px solid ;
                    border-radius: 15px;
                    font-size: 16px;
                    font-weight: bold;
                    color: black;
                    background-color: white;
                    padding: 5px;
                }
            """)
        else:
            line_edit.setStyleSheet("""
                QLineEdit {
                    border: 2px solid rgb(38, 38, 48);
                    border-radius: 15px;
                    font-size: 16px;
                    font-weight: bold;
                    color: rgba(255, 255, 255,255);
                    background-color: rgba(255, 255, 255, 50);
                    padding: 5px;
                }
            """)

class PasswordResetDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Reset Password")
        self.setFixedSize(320, 230)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        self.label_username = QLabel("Username:")
        self.lineEditUsername = QLineEdit()

        self.label_new_password = QLabel("New Password:")
        self.lineEditNewPassword = QLineEdit()
        self.lineEditNewPassword.setEchoMode(QLineEdit.Password)
        self.lineEditNewPassword.setEnabled(False)

        spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.btnConfirm = QPushButton("Confirm")
        self.btnConfirm.setFixedHeight(40)

        layout.addWidget(self.label_username)
        layout.addWidget(self.lineEditUsername)
        layout.addWidget(self.label_new_password)
        layout.addWidget(self.lineEditNewPassword)
        layout.addItem(spacer)
        layout.addWidget(self.btnConfirm)

        self.setLayout(layout)
        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 16px;
                padding: 5px;
                border-radius: 8px;
                border: 2px solid #888;
                background-color: #fff;
            }
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
                background-color: #007bff;
                color: white;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        self.btnConfirm.clicked.connect(self.verify_username)

    def verify_username(self):
        username = self.lineEditUsername.text().strip()
        dc = DataConnector()

        if any(e.UserName == username for e in dc.get_all_managers()):
            self.lineEditNewPassword.setEnabled(True)
            self.btnConfirm.clicked.disconnect()
            self.btnConfirm.clicked.connect(self.update_password)
        else:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng không đúng!")

    def update_password(self):
        username = self.lineEditUsername.text().strip()
        new_password = self.lineEditNewPassword.text().strip()

        if not new_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới không được để trống!")
            return

        dc = DataConnector()
        if dc.updatePassword(username, new_password):
            QMessageBox.information(self, "Thành công", "Mật khẩu đã được cập nhật!")
            self.accept()
        else:
            QMessageBox.warning(self, "Lỗi", "Cập nhật mật khẩu thất bại!")
