from PySide6.QtWidgets import QMessageBox

class PopupBox:
    def __init__(self, parent=None):
        """Cho phép đặt cửa sổ cha nếu cần"""
        self.parent = parent

    def show_warning(self, message):
        """Hiển thị cảnh báo với nền trắng, chữ rõ ràng"""
        msg_box = QMessageBox(self.parent)
        msg_box.setWindowTitle("Cảnh báo")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)  # Icon cảnh báo mặc định
        self.apply_style(msg_box)
        msg_box.exec()

    def show_question(self, message):
        """Hiển thị hộp thoại câu hỏi với nền trắng, chữ rõ ràng"""
        msg_box = QMessageBox(self.parent)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Question)  # Icon dấu hỏi
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.apply_style(msg_box)
        return msg_box.exec()  # Trả về kết quả (Yes hoặc No)

    def show_information(self, message):
        """Hiển thị hộp thoại thông tin với nền trắng, chữ rõ ràng"""
        msg_box = QMessageBox(self.parent)
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # Icon thông tin
        self.apply_style(msg_box)
        msg_box.exec()

    def apply_style(self, msg_box):
        """Áp dụng style cho QMessageBox"""
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: white;
                color: black;
                font-size: 14px;
                border-radius: 10px;
            }
            QLabel {
                background: transparent;
                color: black;
            }
            QPushButton {
                background-color: #763e32;
                color: white;
                border-radius: 5px;
                padding: 6px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #64B5F6;
            }
        """)
