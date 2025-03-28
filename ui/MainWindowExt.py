import json
import os
import re
from datetime import datetime
import random as rd
from functools import partial

import pandas as pd
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize, Qt, QParallelAnimationGroup, QDate
from PySide6.QtGui import QIcon, QPixmap, QIntValidator, QTextDocument, QFont, QColor
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import (
    QPushButton, QFrame, QLabel, QFileDialog, QMessageBox, QSizePolicy, QCompleter, QTableWidgetItem, QDialog,
    QVBoxLayout, QLineEdit, QFormLayout, QComboBox, QHBoxLayout, QSpacerItem, QWidget, QButtonGroup, QGridLayout,
    QTableWidget, QHeaderView, QCheckBox, QCalendarWidget, QAbstractItemView
)
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from libs.JsonFileFactory import JsonFileFactory
from models.Bill import Bill
from models.Customer import Customer
from models.DataConnector import DataConnector
from models.FulltimeEmployee import FullTimeEmployee
from models.Order import Order
from models.ParttimeEmployee import PartTimeEmployee
from models.Product import Product
from ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow  # Lưu lại MainWindow để điều khiển
        self.setupSignalandSlot()
        self.dc = DataConnector()
        self.load_products()
        self.load_menu()
        self.load_employee_data()
        self.load_bieudo()
        self.show_chart_by_week()
        self.show_chart_by_month()
        self.display_total_customers()
        self.bill()
        self.display_total_revenue()
        '''self.load_employees()'''
        self.set_selected_button(self.pushButtonpageOder)
        self.stackedWidget.setCurrentWidget(self.pageOrder)
        self.setup_search_completer_product()
        self.setup_search_completer_employee()
        self.selected_product = None  # Lưu trữ sản phẩm đang chỉnh sửa
        self.selected_category_frame = None
        self.update_category_combobox()
        self.setup_filter_menu()
        # Khởi tạo biến ngày bắt đầu và ngày kết thúc
        self.start_date_str = ""
        self.end_date_str = ""
        self.tableWidgetChamCong.cellClicked.connect(self.update_attendance_status)
        self.status_list = ["Không có lịch", "Đi làm", "Nghỉ có phép", "Nghỉ không phép"]
        self.color_list = [QColor("white"), QColor("green"), QColor("yellow"), QColor("red")]

        self.tableWidgetChamCong.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def setupSignalandSlot(self):
        self.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))

        self.pushButtonpageProduct.clicked.connect(lambda: self.change_page(self.pageProduct, self.pushButtonpageProduct))
        self.pushButtonpageOder.clicked.connect(lambda: self.change_page(self.pageOrder, self.pushButtonpageOder))
        self.pushButtonpageStatistics.clicked.connect(lambda: self.change_page(self.pageStatistics, self.pushButtonpageStatistics))
        self.pushButtonpageEmployee.clicked.connect(lambda: self.change_page(self.pageEmployee, self.pushButtonpageEmployee))
        self.pushButtonpageChamCong.clicked.connect(lambda: self.change_page(self.pageChamCong, self.pushButtonpageChamCong))

        self.pushButtonSave.clicked.connect(self.add_product)
        self.pushButtonAddEmployee.clicked.connect(self.add_employee)

        self.lineEditSearch.textChanged.connect(self.filter_products)
        self.lineEditSearchEmployee.textChanged.connect(self.filter_employees_table)

        self.pushButtonNew.clicked.connect(self.new_product)
        self.pushButtonDelete.clicked.connect(self.delete_product)

        self.pushButtonDeleteEmployee.clicked.connect(self.delete_employee)

        self.pushButton_printBill.clicked.connect(self.export_bill_pdf)
        self.pushButtonDiscount.clicked.connect(self.on_discount_button_clicked)

        self.pushButtonDetails_E.clicked.connect(self.show_schedule_dialog)
        self.pushButtonLoadChamCong.clicked.connect(self.load_attendance_data)

        self.pushButtonSave_Check.clicked.connect(self.save_attendance_to_excel)

    def show_window(self):
        self.MainWindow.show()

##################################################################################
########################### Thiết kế giao diện ###################################
    def change_page(self, page, button):
        """Chuyển trang và cập nhật nút được chọn"""
        self.stackedWidget.setCurrentWidget(page)
        self.set_selected_button(button)

    def set_selected_button(self, selected_button):
        """Cập nhật màu nền và chữ của nút được chọn"""
        buttons = [
            self.pushButtonpageProduct,
            self.pushButtonpageOder,
            self.pushButtonpageEmployee,
            self.pushButtonpageStatistics,
            self.pushButtonpageChamCong,
        ]

        selected_style = """
            QPushButton {
                background-color: #763e32;  /* Màu xanh dương */
                color: white;  /* Chữ trắng */
                font-weight: bold;
                text-align: left;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
        """

        default_style = """
            QPushButton {
                background-color: none;
                color: black;
                text-align: left;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;  /* Thêm dòng này để in đậm */
            }
        """

        for button in buttons:
            if button == selected_button:
                button.setStyleSheet(selected_style)
            else:
                button.setStyleSheet(default_style)

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == standard:
                widthExtended = maxExtend
                self.pushButtonpageProduct.setText("Quản lý sản phẩm")
                self.pushButtonpageOder.setText("Quản lý đơn hàng")
                self.pushButtonpageEmployee.setText("Quản lý nhân viên")
                self.pushButtonpageChamCong.setText("Quản lý chấm công")
                self.pushButtonpageStatistics.setText("Quản lý doanh thu")

                self.frame_toggle.setMaximumWidth(maxExtend)
                self.frame_toggle.setStyleSheet("""
                    background-color: #763e32;
                    border-top-right-radius: 10px; /* Bo tròn góc trên */
                    border-bottom-right-radius: 10px; /* Bo tròn góc dưới */
                    padding: 5px;
                """)
            else:
                widthExtended = standard
                self.pushButtonpageProduct.setText("")
                self.pushButtonpageOder.setText("")
                self.pushButtonpageEmployee.setText("")

                self.frame_toggle.setMaximumWidth(standard)
                self.frame_toggle.setStyleSheet("""
                    background-color: #763e32;
                    border-radius: 0px; /* Không bo tròn khi thu nhỏ */
                    padding: 5px;
                """)

            # 🔥 Animation cho frame_left_menu
            self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)

            # 🔥 Animation cho frame_toggle (giúp bo góc mượt hơn)
            self.animation_toggle = QPropertyAnimation(self.frame_toggle, b"minimumWidth")
            self.animation_toggle.setDuration(400)
            self.animation_toggle.setStartValue(width)
            self.animation_toggle.setEndValue(widthExtended)
            self.animation_toggle.setEasingCurve(QEasingCurve.InOutQuart)

            # 🔥 Chạy animation đồng thời
            self.anim_group = QParallelAnimationGroup()
            self.anim_group.addAnimation(self.animation)
            self.anim_group.addAnimation(self.animation_toggle)
            self.anim_group.start()

    def get_selected_style(self):
        """Trả về style khi button được chọn (màu xanh, chữ trắng)"""
        return """
            QPushButton {
                background-color: #763e32;  /* Màu xanh dương */
                color: white;  /* Chữ trắng */
                font-weight: bold;
                text-align: left;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
        """

    def show_warning(self, message):
        """ Hiển thị cảnh báo với nền trắng, chữ rõ ràng """
        msg_box = QMessageBox(self.MainWindow)
        msg_box.setWindowTitle("Cảnh báo")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)  # Giữ icon cảnh báo mặc định

        # 🔹 Tuỳ chỉnh giao diện QMessageBox
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: white;  /* Nền trắng */
                color: black;  /* Chữ đen */
                font-size: 14px;
                border-radius: 10px;
            }
            QLabel {
                background: transparent; /* Loại bỏ nền đen của chữ */
                color: black;
            }
            QPushButton {
                background-color: #763e32; /* Nút OK màu xanh dương */
                color: white;
                border-radius: 5px;
                padding: 6px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #64B5F6; /* Xanh dương nhạt khi hover */
            }
        """)
        msg_box.exec()

    def show_question(self, message):
        """ Hiển thị hộp thoại câu hỏi với nền trắng, chữ rõ ràng """
        msg_box = QMessageBox(self.MainWindow)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Question)  # Icon dấu hỏi
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # 🔹 Tùy chỉnh giao diện QMessageBox
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: white;  /* Nền trắng */
                color: black;  /* Chữ đen */
                font-size: 14px;
                border-radius: 10px;
            }
            QLabel {
                background: transparent; /* Loại bỏ nền đen của chữ */
                color: black;
            }
            QPushButton {
                background-color: #763e32; /* Nút xanh dương */
                color: white;
                border-radius: 5px;
                padding: 6px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #64B5F6; /* Xanh dương nhạt khi hover */
            }
        """)

        return msg_box.exec()  # Trả về kết quả (Yes hoặc No)

    def show_information(self, message):
        """ Hiển thị hộp thoại thông tin với nền trắng, chữ rõ ràng """
        msg_box = QMessageBox(self.MainWindow)
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # Icon thông tin

        # 🔹 Tùy chỉnh giao diện QMessageBox
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: white;  /* Nền trắng */
                color: black;  /* Chữ đen */
                font-size: 14px;
                border-radius: 10px;
            }
            QLabel {
                background: transparent; /* Loại bỏ nền đen của chữ */
                color: black;
            }
            QPushButton {
                background-color: #763e32; /* Nút xanh dương */
                color: white;
                border-radius: 5px;
                padding: 6px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #64B5F6; /* Xanh dương nhạt khi hover */
            }
        """)

        msg_box.exec()

#############################################################################
########################### Quản sản phẩm ###################################
    def add_frame(self, product):
        """ Thêm một sản phẩm lên giao diện và thiết lập SizePolicy """
        # 🔹 Tạo frame mới
        new_frame = QFrame(self.scrollAreaWidgetContents)
        new_frame.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border-radius: 10px;
            border: 1px solid #ddd;
        """)
        new_frame.setFrameShape(QFrame.Shape.StyledPanel)
        new_frame.setFrameShadow(QFrame.Shadow.Raised)

        # ✅ Đặt SizePolicy thành Expanding
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        new_frame.setSizePolicy(size_policy)
        new_frame.setFixedHeight(100)  # Chỉ cố định chiều cao

        # 🔹 Thêm QPushButton vào frame (dùng để chứa hình ảnh)
        button = QPushButton(new_frame)
        button.setFixedSize(80, 80)
        button.move(10, 10)
        button.setStyleSheet("border: none; background-color: #f8f8f8; border-radius: 10px;")

        # 👉 Thêm ảnh vào button
        if hasattr(product, "image") and product.image:
            image_path = os.path.abspath(product.image)
            if os.path.exists(image_path):
                button.setIcon(QIcon(image_path))
                button.setIconSize(QSize(70, 70))

        # 🔹 Thêm QLabel cho tên sản phẩm
        name_label = QLabel(product.name, new_frame)
        name_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #333; border: none;")
        name_label.move(100, 20)

        # 🔹 Thêm QLabel cho giá sản phẩm
        price_label = QLabel(f"{product.description}", new_frame)
        price_label.setStyleSheet("font-size: 12px; color: #aaa; border: none;")
        price_label.setWordWrap(True)  # Cho phép xuống dòng tự động
        price_label.move(100, 50)

        # ✅ Gán sự kiện click cho frame
        new_frame.mousePressEvent = lambda event, p=product: self.display_product_details(p)

        # 🔹 Thêm frame vào layout
        self.verticalLayout_11.addWidget(new_frame)

    def display_product_details(self, product):
        """ Điền thông tin sản phẩm vào các ô nhập liệu khi bấm vào frame """
        self.lineEditID.setText(product.id)
        self.lineEditName.setText(product.name)
        self.lineEditPrice.setText(str(product.price))
        self.lineEditQuantity.setText(str(product.quantity))
        self.lineEditCategory.setText(product.category)

        index = self.comboBox.findText(product.category)
        if index != -1:
            self.comboBox.setCurrentIndex(index)

    def load_products(self):
        """ Load danh sách sản phẩm từ JSON và hiển thị lên giao diện """
        product_list = self.dc.get_all_products()  # Lấy danh sách sản phẩm

        # Xóa toàn bộ widget cũ (nếu có)
        for i in reversed(range(self.verticalLayout_11.count())):
            widget = self.verticalLayout_11.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Thêm từng sản phẩm vào layout
        for product in product_list:
            self.add_frame(product)  # Truyền đối tượng sản phẩm vào `add_frame`

    def add_product(self):
        """ Cập nhật thông tin sản phẩm hoặc thêm sản phẩm mới """
        old_id = self.lineEditID.property("old_id")  # Lấy ID cũ nếu có
        proid = self.lineEditID.text().strip()
        proname = self.lineEditName.text().strip()
        proprice = self.lineEditPrice.text().strip()
        proquan = self.lineEditQuantity.text().strip()
        procate = self.comboBox.currentText().strip()  # Lấy danh mục từ ComboBox

        errors = []

        # 🔹 Kiểm tra ID sản phẩm
        if not proid:
            errors.append(" ID sản phẩm không được để trống.")
        elif not re.match(r"^[a-zA-Z0-9_-]+$", proid):
            errors.append(" ID sản phẩm chỉ được chứa chữ cái, số, dấu gạch dưới (_) hoặc gạch ngang (-).")

        # 🔹 Kiểm tra tên sản phẩm (chỉ chứa chữ cái và khoảng trắng)
        if not proname:
            errors.append(" Tên sản phẩm không được để trống.")
        elif any(char.isdigit() or not (char.isalpha() or char.isspace()) for char in proname):
            errors.append(" Tên sản phẩm chỉ được chứa chữ cái và khoảng trắng.")

        # 🔹 Kiểm tra giá sản phẩm (có thể là số thập phân)
        try:
            proprice = float(proprice)
            if proprice <= 0:
                errors.append(" Giá sản phẩm phải là số dương.")
        except ValueError:
            errors.append(" Giá sản phẩm phải là số hợp lệ.")

        # 🔹 Kiểm tra số lượng sản phẩm (chỉ chấp nhận số nguyên dương)
        if not proquan.isdigit() or int(proquan) <= 0:
            errors.append(" Số lượng sản phẩm phải là số nguyên dương.")

        # 🔹 Kiểm tra danh mục sản phẩm
        if not procate:
            errors.append(" Vui lòng chọn danh mục sản phẩm.")

        # ✅ Kiểm tra ID có bị trùng không
        jff = JsonFileFactory()
        products = jff.read_data("../datasets/products.json", Product)

        if old_id:  # Đang cập nhật sản phẩm
            existing_product = next((p for p in products if p.id == old_id), None)
            if not existing_product:
                errors.append("Sản phẩm cần cập nhật không tồn tại.")

            elif old_id != proid and any(p.id == proid for p in products):
                errors.append("ID mới đã tồn tại! Vui lòng chọn ID khác.")

        else:  # Đang thêm mới sản phẩm
            if any(p.id == proid for p in products):
                errors.append("ID sản phẩm đã tồn tại! Vui lòng chọn ID khác.")

        # ✅ Nếu có lỗi thì báo tất cả lỗi và dừng lại
        if errors:
            self.show_warning("\n".join(errors))
            return

        # ✅ Nếu không có lỗi, mở hộp thoại chọn ảnh
        image_path, _ = QFileDialog.getOpenFileName(self.MainWindow, "Chọn ảnh sản phẩm", "",
                                                    "Images (*.png *.jpg *.jpeg *.bmp)")

        if not image_path:
            self.show_warning("Vui lòng chọn ảnh sản phẩm!")
            return

        # ✅ Tiến hành cập nhật hoặc thêm sản phẩm
        if old_id:
            # Cập nhật sản phẩm
            existing_product.id = proid
            existing_product.name = proname
            existing_product.category = procate
            existing_product.price = str(proprice)  # Chuyển về string để lưu JSON
            existing_product.quantity = proquan
            existing_product.image = image_path
            self.show_information(" Sản phẩm đã được cập nhật!")

        else:
            # Thêm sản phẩm mới
            new_product = Product(proid, proname, procate, str(proprice), proquan, image_path)
            products.append(new_product)
            self.show_information( " Sản phẩm mới đã được thêm!")

        # ✅ Ghi dữ liệu mới vào JSON
        jff.write_data(products, "../datasets/products.json")

        # ✅ Tải lại danh sách sản phẩm để cập nhật UI
        self.load_products()

    def new_product(self):
        """ Xóa thông tin sản phẩm đang chỉnh sửa để tạo mới """
        self.selected_product = None
        self.lineEditID.setText("")
        self.lineEditName.setText("")
        self.lineEditCategory.setText("")
        self.lineEditQuantity.setText("")
        self.lineEditPrice.setText("")
        self.lineEditID.setFocus()

    def update_category_combobox(self):
        categories = self.load_categories()  # Gọi hàm load danh mục
        self.comboBox.clear()
        self.comboBox.addItem("All")  # Thêm tùy chọn xem tất cả
        self.comboBox.addItems(categories)

    def load_categories(self):
        try:
            jff = JsonFileFactory()
            categories = jff.read_data("../datasets/categories.json", list)
            if not isinstance(categories, list):
                raise ValueError("Dữ liệu danh mục không phải là danh sách!")
            return categories
        except Exception as e:
            print(f"Lỗi khi load danh mục: {e}")
            return []  # Trả về danh sách rỗng nếu có lỗi

    def delete_product(self):
        """ Xóa sản phẩm đang được chọn """
        proid = self.lineEditID.text().strip()

        if not proid:
            self.show_warning("Vui lòng chọn sản phẩm cần xóa!")
            return

        # Xác nhận trước khi xóa
        reply = self.show_question(f"Bạn có chắc chắn muốn xóa sản phẩm có ID {proid} không?")

        if reply != QMessageBox.StandardButton.Yes:
            return

        # Đọc dữ liệu sản phẩm từ JSON
        jff = JsonFileFactory()
        products = jff.read_data("../datasets/products.json", Product)

        # Lọc sản phẩm cần xóa
        updated_products = [p for p in products if p.id != proid]

        # Kiểm tra sản phẩm có tồn tại không
        if len(products) == len(updated_products):
            self.show_warning("Sản phẩm không tồn tại!")
            return

        # Ghi lại danh sách sản phẩm sau khi xóa
        jff.write_data(updated_products, "../datasets/products.json")

        self.show_information("🎉 Sản phẩm đã được xóa!")

        # Xóa thông tin trên giao diện và tải lại danh sách
        self.new_product()
        self.load_products()

    def setup_search_completer_product(self):
        """Thiết lập gợi ý tìm kiếm với QCompleter"""
        product_names = [product.name for product in self.dc.get_all_products()]
        self.completer = QCompleter(product_names, self.MainWindow)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.activated.connect(self.on_completer_selected_product)
        self.lineEditSearch.setCompleter(self.completer)
        self.comboBox.currentIndexChanged.connect(self.filter_products)

    def on_completer_selected_product(self, text):
        """Khi chọn một gợi ý, tự động cập nhật ô tìm kiếm và lọc danh sách"""
        self.lineEditSearch.setText(text)
        self.filter_products()

    def filter_products(self):
        """Lọc danh sách sản phẩm dựa trên nội dung tìm kiếm"""
        search_text = self.lineEditSearch.text().strip().lower()
        selected_category = self.comboBox.currentText().strip()  # Lấy danh mục từ comboBox

        # Lấy toàn bộ sản phẩm
        all_products = self.dc.get_all_products()

        # Lọc theo tên sản phẩm nếu có tìm kiếm
        filtered_products = [p for p in all_products if search_text in p.name.lower()] if search_text else all_products

        # Lọc theo danh mục nếu danh mục không phải "All"
        if selected_category and selected_category != "All":
            filtered_products = [p for p in filtered_products if p.category.lower() == selected_category.lower()]

        # Xóa toàn bộ sản phẩm hiện tại trong UI
        for i in reversed(range(self.verticalLayout_11.count())):
            widget = self.verticalLayout_11.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Hiển thị danh sách sản phẩm đã lọc
        for product in filtered_products:
            self.add_frame(product)


#############################################################################
######################## Quản lý đơn hàng + menu  ###########################
    def setup_filter_menu(self):
        """Tạo danh mục sản phẩm với khoảng cách đều nhau và không bị dư ảnh default"""
        categories = self.load_categories()
        if "All" not in categories:  # Đảm bảo danh mục "All" luôn có
            categories.insert(0, "All")

        category_images = {
            "All": "../images/all.png",
            "Coffee": "../images/coffee.png",
            "Tea": "../images/tea (2).png",
            "Juice": "../images/juice.png",
        }

        # Xóa danh mục cũ
        while self.horizontalLayoutFilterMenu.count():
            item = self.horizontalLayoutFilterMenu.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Thêm spacer trái để căn giữa danh mục
        self.horizontalLayoutFilterMenu.addSpacerItem(
            QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )

        added_categories = set()
        all_frame = None  # Lưu frame của "All" để chọn mặc định

        for category in categories:
            category_name = category if isinstance(category, str) else category.get("name", "Unknown")

            if category_name in added_categories:
                continue
            added_categories.add(category_name)

            image_path = category_images.get(category_name, "../images/default.png")
            if not os.path.exists(image_path):
                image_path = "../images/default.png"

            frame = QFrame()
            frame.setFixedSize(80, 80)
            frame.setStyleSheet("""
                QFrame {
                    border-radius: 10px;
                    background-color: white;
                    border: 2px solid transparent;
                }
            """)

            v_layout = QVBoxLayout(frame)
            v_layout.setSpacing(5)
            v_layout.setContentsMargins(5, 5, 5, 5)

            img_label = QLabel()
            pixmap = QPixmap(image_path)
            img_label.setPixmap(
                pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            )
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            img_label.setStyleSheet("border: none; background: transparent;")

            text_label = QLabel(category_name)
            text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            text_label.setStyleSheet("border: none; background: transparent; font-size: 12px; color: black;")

            v_layout.addWidget(img_label)
            v_layout.addWidget(text_label)

            frame.mousePressEvent = lambda event, name=category_name, f=frame: self.on_category_selected(name, f)

            # Nếu là danh mục "All", lưu lại frame để chọn mặc định
            if category_name == "All":
                all_frame = frame

            self.horizontalLayoutFilterMenu.addWidget(frame)

        # Thêm spacer phải để căn giữa danh mục
        self.horizontalLayoutFilterMenu.addSpacerItem(
            QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )

        # Chọn mặc định danh mục "All" nếu tồn tại
        if all_frame:
            self.on_category_selected("All", all_frame)

    def update_brief_information(self, category_name, total_items):
        """Cập nhật tiêu đề menu và số lượng sản phẩm"""

        if category_name == "All":
            self.label_10.setText("All Products")
            self.label_5.setText(f"{total_items} items available")
        else:
            self.label_10.setText(f"{category_name} Menu")
            self.label_5.setText(f"{total_items} {category_name.lower()} results")

    def get_products_by_category(self, category_id):
        """Lọc sản phẩm theo danh mục, bao gồm cả 'All' để hiển thị tất cả"""
        if category_id == "All":
            return self.dc.get_all_products()  # Trả về toàn bộ sản phẩm
        return [product for product in self.dc.get_all_products() if product.category == category_id]

    def on_category_selected(self, category_name, selected_frame):
        """Xử lý khi click vào danh mục - Cập nhật giao diện và hiển thị sản phẩm thuộc danh mục đó"""

        # Bỏ hiệu ứng của danh mục cũ nếu có
        if hasattr(self, 'selected_category_frame') and self.selected_category_frame:
            self.selected_category_frame.setStyleSheet("""
                QFrame {
                    border-radius: 10px;
                    background-color: white;
                    border: 2px solid transparent; /* Bỏ viền */
                }
            """)

        # Gán danh mục mới được chọn
        self.selected_category_frame = selected_frame
        selected_frame.setStyleSheet("""
            QFrame {
                border-radius: 10px;
                background-color: #f7f3f0; /* Màu nền nâu nhạt */
                border: 3px solid #8b5e3c; /* Viền nâu */
            }
        """)

        # 🎯 Lọc danh sách sản phẩm theo danh mục
        filtered_products = self.get_products_by_category(category_name)

        # Cập nhật thông tin danh mục
        total_items = len(filtered_products)
        self.update_brief_information(category_name, total_items)

        # 🛒 Load menu với danh sách sản phẩm đã lọc
        self.load_menu(filtered_products)

    def create_product_frame(self, product):
        """Tạo một frame chứa thông tin sản phẩm với bố cục nhỏ gọn hơn"""
        new_frame = QFrame()
        new_frame.setFixedSize(230, 350)  # Giảm kích thước frame
        new_frame.setStyleSheet("""
            QFrame {
                background-color: #fff;
                border-radius: 12px;
                border: none;
                padding: 6px;
            }
        """)

        main_layout = QVBoxLayout(new_frame)
        main_layout.setContentsMargins(6, 6, 6, 6)
        main_layout.setSpacing(4)

        # 🏗️ Phần trên: Ảnh + Thông tin sản phẩm
        top_frame = QFrame()
        top_layout = QHBoxLayout(top_frame)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(6)

        # 🖼 Hình ảnh sản phẩm
        image_label = QLabel()
        if hasattr(product, "image") and product.image:
            image_path = os.path.abspath(product.image)
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path).scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio,
                                                    Qt.TransformationMode.SmoothTransformation)
                image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setStyleSheet("border: none;")

        # 📄 Thông tin sản phẩm
        info_layout = QVBoxLayout()
        name_label = QLabel(f"{product.name}")
        name_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #333;")

        desc_label = QLabel(f"{product.description}")
        desc_label.setStyleSheet("font-size: 12px; color: #777;")
        desc_label.setWordWrap(True)  # Cho phép xuống dòng tự động

        price_label = QLabel(f"<b>{product.price} VND</b>")
        price_label.setStyleSheet("color: #d35400; font-size: 14px; font-weight: bold;")

        info_layout.addWidget(name_label)
        info_layout.addWidget(desc_label)
        info_layout.addWidget(price_label)

        top_layout.addWidget(image_label)
        top_layout.addLayout(info_layout)
        top_frame.setLayout(top_layout)

        # 🏗️ Phần dưới: Tùy chọn size, đường, đá + nút đặt hàng
        bottom_frame = QFrame()
        bottom_layout = QVBoxLayout(bottom_frame)
        bottom_layout.setSpacing(4)

        option_layout = QGridLayout()
        option_layout.setSpacing(4)

        # 🔹 Tạo nhóm nút riêng cho từng sản phẩm
        size_group = QButtonGroup(new_frame)
        sugar_group = QButtonGroup(new_frame)
        ice_group = QButtonGroup(new_frame)

        # Chỉ cho phép chọn 1 nút trong mỗi nhóm
        size_group.setExclusive(True)
        sugar_group.setExclusive(True)
        ice_group.setExclusive(True)

        # Tiêu đề các tùy chọn
        size_label = QLabel("Size:")
        sugar_label = QLabel("Sugar:")
        ice_label = QLabel("Ice:")

        for lbl in [size_label, sugar_label, ice_label]:
            lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none;")

        option_layout.addWidget(size_label, 0, 0)
        option_layout.addWidget(sugar_label, 1, 0)
        option_layout.addWidget(ice_label, 2, 0)

        button_size = 25  # Giảm kích thước nút

        # 🔹 Nút chọn Size
        size_prices = {"S": 0, "M": 5000, "L": 10000}  # Giá thay đổi theo size

        for i, size in enumerate(["S", "M", "L"]):
            btn = QPushButton(size)
            btn.setCheckable(True)
            btn.setFixedSize(button_size, button_size)
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 12px;
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    font-size: 10px;
                }
                QPushButton:checked {
                    background-color: #8B4513;
                    color: white;
                }
            """)
            size_group.addButton(btn)  # Thêm vào nhóm
            option_layout.addWidget(btn, 0, i + 1)

            # Khi nút size được chọn, cập nhật giá
            btn.clicked.connect(partial(self.update_product_price, size, price_label, product))

        # 🔹 Nút chọn Sugar
        for i, level in enumerate(["30%", "50%", "70%"]):
            btn = QPushButton(level)
            btn.setCheckable(True)
            btn.setFixedSize(button_size, button_size)
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 12px;
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    font-size: 10px;
                }
                QPushButton:checked {
                    background-color: #8B4513;
                    color: white;
                }
            """)
            sugar_group.addButton(btn)
            option_layout.addWidget(btn, 1, i + 1)

        # 🔹 Nút chọn Ice
        for i, level in enumerate(["30%", "50%", "70%"]):
            btn = QPushButton(level)
            btn.setCheckable(True)
            btn.setFixedSize(button_size, button_size)
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 12px;
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    font-size: 10px;
                }
                QPushButton:checked {
                    background-color: #8B4513;
                    color: white;
                }
            """)
            ice_group.addButton(btn)
            option_layout.addWidget(btn, 2, i + 1)

        bottom_layout.addLayout(option_layout)

        # 🛒 Nút thêm vào hóa đơn
        add_button = QPushButton("Add")
        add_button.setFixedSize(80, 30)  # Giảm kích thước nút
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #8B4513;
                color: white;
                border-radius: 8px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #A0522D;
            }
        """)
        bottom_layout.addWidget(add_button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(top_frame)
        main_layout.addWidget(bottom_frame)

        new_frame.setLayout(main_layout)

        add_button.clicked.connect(lambda: self.add_to_order(product, price_label))  # Cập nhật khi nhấn "Add to Order"

        return new_frame

    def update_product_price(self, size, price_label, product):
        """Cập nhật giá sản phẩm khi chọn size"""
        size_prices = {"S": 0, "M": 5000, "L": 15000}  # Giá thay đổi theo size
        base_price = product.price
        if size in size_prices:
            new_price = base_price + size_prices[size]
            price_label.setText(f"<b>{new_price} VND</b>")
        else:
            price_label.setText(f"<b>{base_price} VND</b>")

    def load_menu(self, product_list=None):
        """ Load danh sách sản phẩm từ JSON và hiển thị lên giao diện với bố cục 2 cột """
        if product_list is None:
            product_list = self.dc.get_all_products()

        while self.gridLayout_ProductMenu.count():
            widget = self.gridLayout_ProductMenu.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        columns = 2  # Giới hạn còn 2 cột
        self.gridLayout_ProductMenu.setHorizontalSpacing(10)
        self.gridLayout_ProductMenu.setVerticalSpacing(10)
        self.gridLayout_ProductMenu.setAlignment(Qt.AlignmentFlag.AlignTop)

        for index, product in enumerate(product_list):
            row = index // columns
            col = index % columns
            frame = self.create_product_frame(product)
            self.gridLayout_ProductMenu.addWidget(frame, row, col)

        items_in_last_row = len(product_list) % columns
        if items_in_last_row > 0:
            for _ in range(columns - items_in_last_row):
                self.gridLayout_ProductMenu.addItem(QSpacerItem(10, 10), row, col + 1)

    def add_to_order(self, product, price_label):
        """Thêm sản phẩm vào danh sách order"""

        # Lấy giá hiện tại từ price_label và tính toán
        price_text = price_label.text().replace("<b>", "").replace(" VND</b>", "")
        price = int(price_text.replace(",", ""))

        # Tạo khung chứa sản phẩm trong đơn hàng
        order_frame = QFrame()
        order_frame.setStyleSheet("background-color: white; border: 1px solid #ccc; border-radius: 5px;")
        order_frame.setFixedHeight(40)

        layout = QHBoxLayout(order_frame)
        layout.setContentsMargins(10, 2, 10, 2)
        layout.setSpacing(15)

        # Tên sản phẩm
        name_label = QLabel(product.name)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333; border: none;")
        layout.addWidget(name_label)

        # Giá sản phẩm
        price_label = QLabel(f"{price:,} VND")
        price_label.setStyleSheet("font-size: 14px; color: #555; border: none;")
        layout.addWidget(price_label)

        # Nút giảm số lượng
        btn_minus = QPushButton("-")
        btn_minus.setFixedSize(25, 25)
        btn_minus.setStyleSheet("font-size: 14px;")
        layout.addWidget(btn_minus)

        # Ô nhập số lượng
        quantity_input = QLineEdit("1")
        quantity_input.setFixedWidth(40)
        quantity_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        quantity_input.setValidator(QIntValidator(0, 999))
        quantity_input.setStyleSheet("font-size: 14px; padding: 5px; text-align: center;")
        layout.addWidget(quantity_input)

        # Nút tăng số lượng
        btn_plus = QPushButton("+")
        btn_plus.setFixedSize(25, 25)
        btn_plus.setStyleSheet("font-size: 14px;")
        layout.addWidget(btn_plus)

        # Tổng giá của sản phẩm này
        total_price_label = QLabel(f"{price:,} VND")
        total_price_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333; border: none;")
        layout.addWidget(total_price_label)

        # Hàm cập nhật tổng tiền
        def update_total_price():
            try:
                quantity = int(quantity_input.text())
                if quantity == 0:
                    order_frame.setParent(None)  # Xóa sản phẩm khỏi giao diện
                else:
                    total_price_label.setText(f"{quantity * price:,} VND")
                self.update_total_payment()  # Cập nhật tổng tiền
            except ValueError:
                quantity_input.setText("1")

        # Kết nối sự kiện tăng/giảm số lượng
        btn_minus.clicked.connect(lambda: quantity_input.setText(str(max(0, int(quantity_input.text()) - 1))))
        btn_plus.clicked.connect(lambda: quantity_input.setText(str(int(quantity_input.text()) + 1)))
        quantity_input.textChanged.connect(update_total_price)

        # Đảm bảo total_price_label luôn ở dưới cùng
        if not hasattr(self, "total_price_label"):
            self.total_price_label = QLabel("Tổng tiền: 0 VND")
            self.total_price_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.total_price_label.setStyleSheet(
                "font-size: 16px; font-weight: bold; color: #d32f2f; border: none; margin-top: 10px;")
            self.verticalLayout_Order.addWidget(self.total_price_label)

        # Thêm sản phẩm vào danh sách
        self.verticalLayout_Order.insertWidget(self.verticalLayout_Order.count() - 1, order_frame)

        # Cập nhật tổng tiền ngay khi thêm sản phẩm
        self.update_total_payment()

    def export_bill_pdf(self):
        """Xuất hóa đơn ra file PDF và lưu thông tin vào JSON"""

        bill_json = "../datasets/bills.json"
        customers_json = "../datasets/customers.json"
        jff = JsonFileFactory()

        # Lấy thông tin khách hàng từ giao diện
        customer_name = self.lineEditCustomerName.text().strip() or "Khách hàng không tên"
        phone_number = self.lineEditCustomerPhoneNumber.text().strip() or "0000000000"
        order_time = datetime.now().strftime("%H:%M %d/%m/%Y")
        total_payment = 0

        # Lấy danh sách sản phẩm từ giao diện
        order_items = []
        for i in range(self.verticalLayout_Order.count() - 1):
            item = self.verticalLayout_Order.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                labels = widget.findChildren(QLabel)
                line_edits = widget.findChildren(QLineEdit)

                if labels and line_edits:
                    product_name = labels[0].text()
                    price = int(labels[1].text().replace(" VND", "").replace(",", ""))
                    quantity = int(line_edits[0].text())
                    total_price = price * quantity

                    # Tạo đối tượng Order và thêm vào danh sách order_items
                    order_items.append(Order(product_name, quantity, total_price))
                    total_payment += total_price

        # Kiểm tra điểm của khách hàng và áp dụng giảm giá
        try:
            customers_data_list = jff.read_data(customers_json, Customer)
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu từ {customers_json}: {e}")
            customers_data_list = []

        customer_points = 0
        for customer in customers_data_list:
            if customer.phone == phone_number:
                customer_points = customer.points
                break

        # Áp dụng giảm giá nếu đủ điểm (truyền đúng các đối số)
        total_payment = self.discount(total_payment, customer_points)

        # Tạo và lưu hóa đơn như bình thường
        file_path, _ = QFileDialog.getSaveFileName(self.MainWindow, "Lưu hóa đơn", "", "PDF Files (*.pdf)")
        if not file_path:
            return  # Người dùng bấm Hủy

        # Tạo nội dung hóa đơn HTML
        bill_content = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; font-size: 16px; text-align: center; }}
                table {{ width: 80%; border-collapse: collapse; margin-left: auto; margin-right: auto; }}
                th, td {{ border: 1px solid black; padding: 10px; text-align: center; }}
                th {{ background-color: #ddd; font-size: 18px; }}
                .total {{ font-weight: bold; font-size: 20px; color: red; text-align: right; padding-right: 5%; }}
                .thankyou {{ text-align: center; margin-top: 15px; font-size: 14px; }}
            </style>
        </head>
        <body>
            <h1>COFFEE BINBO</h1>
            <p>KCN BẮC ĐỒNG PHÚ, TT TÂN PHÚ.<br>0904813138</p>
            <h2>HÓA ĐƠN BÀN 10</h2>
            <p><b>Giờ bắt đầu:</b> {order_time}</p>
            <p><b>Khách hàng:</b> {customer_name} | <b>SĐT:</b> {phone_number}</p>

            <table>
                <tr>
                    <th>Tên</th>
                    <th>SL</th>
                    <th>Giá</th>
                    <th>Tổng</th>
                </tr>
        """

        for item in order_items:
            bill_content += f"""
            <tr>
                <td>{item.product_name}</td>
                <td>{item.quantity}</td>
                <td>{item.total_price:,} VND</td>
                <td>{item.total_price:,} VND</td>
            </tr>
            """

        bill_content += f"""
            </table>
            <p class="total">Tổng dịch vụ: {total_payment:,} VND</p>
            <h2 class="bold">THANH TOÁN: {total_payment:,} VND</h2>
            <p><b>Mã hóa đơn:</b> {rd.randint(1000, 9999)}</p>
            <p><b>Thu ngân:</b> Nguyễn Duy Quang</p>

            <p class="thankyou">
                Quý khách vui lòng kiểm tra lại hóa đơn trước khi thanh toán.<br>
                Xin cảm ơn quý khách.<br>
                Hẹn gặp lại quý khách lần sau.
            </p>
        </body>
        </html>
        """

        # Lưu file PDF
        doc = QTextDocument()
        doc.setHtml(bill_content)
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(file_path)
        doc.print_(printer)

        # Lưu thông tin vào file JSON
        bill_data = Bill(customer_name, phone_number, file_path.split('/')[-1])

        # Đọc dữ liệu từ file JSON bằng jff
        try:
            bills_data = jff.read_data(bill_json, Bill)  # Đọc dữ liệu từ bills.json (dựng dạng dict)
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu từ {bill_json}: {e}")
            bills_data = []  # Nếu có lỗi thì khởi tạo danh sách rỗng
        # Thêm thông tin hóa đơn vào danh sách
        bills_data.append(bill_data)

        jff = JsonFileFactory()
        try:
            customers_data_list = jff.read_data(customers_json, Customer)
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu từ {customers_json}: {e}")
            customers_data_list = []  # Nếu có lỗi, tạo danh sách rỗng

        # Kiểm tra xem khách hàng đã có trong danh sách chưa
        customer_found = False
        for customer in customers_data_list:
            if customer.phone == phone_number:
                # Nếu khách hàng đã tồn tại, cập nhật thông tin
                customer_found = True
                customer.total_payment += total_payment  # Cộng dồn tổng tiền
                customer.points += total_payment // 1000  # Cộng dồn điểm tích lũy
                customer.last_transaction_time = order_time
                break

        # Nếu khách hàng chưa có, tạo mới khách hàng và thêm vào danh sách
        if not customer_found:
            new_customer = Customer(customer_name, phone_number)
            new_customer.total_payment = total_payment
            new_customer.points = total_payment // 1000
            new_customer.last_transaction_time = order_time
            customers_data_list.append(new_customer)

        # Ghi lại dữ liệu vào file JSON
        jff.write_data(customers_data_list, customers_json)

        # Ghi lại dữ liệu vào file JSON
        jff.write_data(bills_data, bill_json)

        print(f"📄 Hóa đơn đã lưu tại: {file_path}")
        print(f"💾 Đã lưu thông tin hóa đơn của khách {customer_name} vào {bill_json}")

    def get_current_time(self):
        """Hàm lấy thời gian hiện tại để hiển thị trên hóa đơn"""
        from datetime import datetime
        return datetime.now().strftime("%H:%M %d/%m/%Y")

    def discount(self, total_price, customer_points):
        """Giảm giá 50,000 VND nếu khách hàng có 1000 điểm tích lũy"""
        discount_amount = 50000 if customer_points >= 1000 else 0
        final_price = max(0, total_price - discount_amount)  # Đảm bảo giá không âm

        # Nếu giảm giá thành công, cập nhật lại điểm trong JSON
        if discount_amount > 0:
            # Lấy số điện thoại của khách hàng từ ô nhập liệu
            phone_number = self.lineEditCustomerPhoneNumber.text().strip() or "0000000000"

            # Cập nhật lại điểm trong file JSON (truyền cả phone_number và số điểm mới)
            self.update_customer_points(phone_number,
                                        customer_points - 1000)  # Trừ đi 1000 điểm sau khi áp dụng giảm giá

        return final_price

    def on_discount_button_clicked(self):
        """Hàm được gọi khi nhấn nút giảm giá"""
        self.update_total_payment()  # Cập nhật lại tổng tiền và điểm khách hàng

    def update_total_payment(self):
        total_payment = 0
        # Tính tổng tiền của tất cả các sản phẩm trong giỏ hàng
        for i in range(self.verticalLayout_Order.count()):
            item = self.verticalLayout_Order.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                total_labels = widget.findChildren(QLabel)
                if total_labels:
                    total_text = total_labels[-1].text().replace(",", "").replace(" VND", "")
                    total_payment += int(total_text) if total_text.isdigit() else 0

        # Lấy điểm khách hàng từ dữ liệu
        customer_points = 0
        phone_number = self.lineEditCustomerPhoneNumber.text().strip() or "0000000000"

        # Lấy danh sách khách hàng từ file JSON
        customers_data_list = self.dc.get_customers_data()

        for customer in customers_data_list:
            if customer.phone == phone_number:
                customer_points = customer.points
                break

        # Áp dụng giảm giá nếu khách hàng đủ điểm
        total_payment = self.discount(total_payment, customer_points)  # Giảm giá

        # Cập nhật lại tổng tiền sau giảm giá
        self.total_price_label.setText(f"Tổng tiền: {total_payment:,} VND")

    def update_customer_points(self, phone_number, new_points):
        """Cập nhật điểm tích lũy của khách hàng vào file JSON"""
        customers_json = "../datasets/customers.json"
        jff = JsonFileFactory()

        try:
            customers_data_list = jff.read_data(customers_json, Customer)
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu từ {customers_json}: {e}")
            customers_data_list = []  # Nếu có lỗi, tạo danh sách rỗng

        customer_found = False
        for customer in customers_data_list:
            if customer.phone == phone_number:
                customer_found = True
                customer.points = new_points  # Cập nhật lại điểm
                break

        if customer_found:
            # Ghi lại dữ liệu vào file JSON
            jff.write_data(customers_data_list, customers_json)
            print(f"Điểm của khách hàng {phone_number} đã được cập nhật thành {new_points}.")
        else:
            print(f"Khách hàng với SĐT {phone_number} không tìm thấy.")


#############################################################################
######################## Quản lý nhân viên #################################

    #tìm kiếm sản phẩm dựa trên tên sản phẩm
    def setup_search_completer_employee(self):
        """Thiết lập QCompleter và kết nối sự kiện tìm kiếm nhân viên"""
        emp_names = [emp.name for emp in self.dc.get_all_employees()]
        self.completer = QCompleter(emp_names, self.MainWindow)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.activated.connect(self.on_completer_selected_employee)
        self.lineEditSearchEmployee.setCompleter(self.completer)
        self.lineEditSearchEmployee.textChanged.connect(self.filter_employees_table)

    def on_completer_selected_employee(self, text):
        """Cập nhật ô tìm kiếm và lọc bảng khi chọn gợi ý nhân viên"""
        self.lineEditSearchEmployee.setText(text)
        self.filter_employees_table()

    def filter_employees_table(self):
        """Lọc danh sách nhân viên trên QTableWidget theo tên"""
        search_text = self.lineEditSearchEmployee.text().strip().lower()

        if self.tableWidgetEmployee.rowCount() == 0:
            print("⚠ Không có dữ liệu trong bảng nhân viên!")
            return

        found = False  # Kiểm tra xem có nhân viên nào khớp không

        for row in range(self.tableWidgetEmployee.rowCount()):
            item = self.tableWidgetEmployee.item(row, 1)  # Cột 1 là "Họ và Tên"
            if item:
                emp_name = item.text().strip().lower()
                match = search_text in emp_name
                self.tableWidgetEmployee.setRowHidden(row, not match)
                if match:
                    found = True  # Đánh dấu tìm thấy ít nhất một nhân viên

        if not found:
            print(f"❌ Không tìm thấy nhân viên nào khớp với: {search_text}")

    def load_employee_data(self):
        """Load danh sách nhân viên từ DataConnector vào QTableWidget"""
        employees = self.dc.get_all_employees()  # Lấy danh sách nhân viên từ JSON

        if not employees:  # Nếu employees là None hoặc rỗng
            print("⚠ Không có dữ liệu nhân viên!")
            return

        self.tableWidgetEmployee.setRowCount(len(employees))  # Cập nhật số dòng trong bảng
        self.tableWidgetEmployee.setColumnCount(6)  # Hiển thị 6 cột cần thiết
        self.tableWidgetEmployee.setHorizontalHeaderLabels(
            ["ID", "Họ và Tên", "Ngày sinh", "Số điện thoại", "Vị trí", "Ngày vào làm"]
        )

        for row, emp in enumerate(employees):
            self.tableWidgetEmployee.setItem(row, 0, QTableWidgetItem(str(emp.id)))
            self.tableWidgetEmployee.setItem(row, 1, QTableWidgetItem(emp.name))
            self.tableWidgetEmployee.setItem(row, 2, QTableWidgetItem(emp.date_of_birth))
            self.tableWidgetEmployee.setItem(row, 3, QTableWidgetItem(emp.phone_number))
            self.tableWidgetEmployee.setItem(row, 4, QTableWidgetItem(emp.position))
            self.tableWidgetEmployee.setItem(row, 5, QTableWidgetItem(emp.start_working_date))

    def add_employee(self):
        """Mở cửa sổ nhập nhân viên, kiểm tra lỗi, lưu vào JSON và cập nhật QTableWidget"""

        prev_data = {
            "id": "", "name": "", "dob": "", "phone": "",
            "position": "", "start_date": "", "type": "Full-time"
        }

        while True:
            dialog = QDialog(self.MainWindow)
            dialog.setWindowTitle("Thêm Nhân Viên Mới")
            dialog.setFixedSize(400, 350)
            dialog.setStyleSheet("background-color: white;")

            layout = QVBoxLayout(dialog)
            form_layout = QFormLayout()

            id_input = QLineEdit(prev_data["id"])
            name_input = QLineEdit(prev_data["name"])
            dob_input = QLineEdit(prev_data["dob"])
            phone_input = QLineEdit(prev_data["phone"])

            position_input = QComboBox()
            position_input.addItems(["Phục vụ", "Thu ngân", "Pha chế"])
            position_input.setCurrentText(prev_data["position"])

            start_date_input = QLineEdit(prev_data["start_date"])
            emp_type_input = QComboBox()
            emp_type_input.addItems(["Full-time", "Part-time"])
            emp_type_input.setCurrentText(prev_data["type"])

            form_layout.addRow("Mã nhân viên:", id_input)
            form_layout.addRow("Họ và tên:", name_input)
            form_layout.addRow("Ngày sinh (YYYY-MM-DD):", dob_input)
            form_layout.addRow("Số điện thoại:", phone_input)
            form_layout.addRow("Vị trí:", position_input)
            form_layout.addRow("Ngày vào làm (YYYY-MM-DD):", start_date_input)
            form_layout.addRow("Loại nhân viên:", emp_type_input)

            save_button = QPushButton("Thêm")
            save_button.clicked.connect(dialog.accept)

            layout.addLayout(form_layout)
            layout.addWidget(save_button)
            dialog.setLayout(layout)

            if dialog.exec() == 0:
                return  # Người dùng đóng form

            emp_id = id_input.text().strip()
            emp_name = name_input.text().strip()
            emp_dob = dob_input.text().strip()
            emp_phone = phone_input.text().strip()
            emp_position = position_input.currentText()
            emp_start_date = start_date_input.text().strip()
            emp_type = emp_type_input.currentText()

            prev_data = {
                "id": emp_id, "name": emp_name, "dob": emp_dob, "phone": emp_phone,
                "position": emp_position, "start_date": emp_start_date, "type": emp_type
            }

            errors = []

            if not emp_id:
                errors.append("Mã nhân viên không được để trống.")
            if not emp_name or any(char.isdigit() for char in emp_name):
                errors.append("Họ và tên chỉ được chứa chữ cái và khoảng trắng.")
            if not emp_phone.isdigit() or len(emp_phone) < 10:
                errors.append("Số điện thoại không hợp lệ! Chỉ chứa số và tối thiểu 9 chữ số.")
            date_pattern = r"^\d{4}-\d{2}-\d{2}$"
            if not re.match(date_pattern, emp_dob):
                errors.append("Ngày sinh không hợp lệ! Định dạng đúng: YYYY-MM-DD.")
            if not re.match(date_pattern, emp_start_date):
                errors.append("Ngày vào làm không hợp lệ! Định dạng đúng: YYYY-MM-DD.")

            # ✅ Đọc danh sách nhân viên từ JSON
            jff = JsonFileFactory()
            employees_data = jff.read_data("../datasets/employees.json", dict)  # Đọc JSON dưới dạng dict

            employees = []
            for data in employees_data:
                emp_class = FullTimeEmployee if data.get("employee_type",
                                                         "Full-time") == "Full-time" else PartTimeEmployee
                valid_params = emp_class.__init__.__code__.co_varnames
                filtered_data = {k: v for k, v in data.items() if k in valid_params}
                employees.append(emp_class(**filtered_data))

            if any(emp.id == emp_id for emp in employees):
                errors.append("Mã nhân viên đã tồn tại! Vui lòng chọn mã khác.")

            if errors:
                self.show_warning("\n".join(errors))
                continue  # Quay lại vòng lặp nhập lại

            # ✅ Tạo nhân viên mới
            emp_class = FullTimeEmployee if emp_type == "Full-time" else PartTimeEmployee
            valid_params = emp_class.__init__.__code__.co_varnames
            new_employee_data = {
                "id": emp_id, "name": emp_name, "date_of_birth": emp_dob,
                "phone_number": emp_phone, "position": emp_position,
                "employee_type": emp_type, "start_working_date": emp_start_date
            }
            new_employee = emp_class(**{k: v for k, v in new_employee_data.items() if k in valid_params})

            employees.append(new_employee)
            jff.write_data(employees, "../datasets/employees.json")

            self.load_employee_data()
            self.show_information("Nhân viên mới đã được thêm!")
            break

    def show_schedule_dialog(self):
        """Hiển thị dialog xếp lịch với nút chọn ngày bắt đầu & kết thúc"""
        dialog = QDialog(self.MainWindow)
        dialog.setWindowTitle("Xếp Lịch Nhân Viên")
        dialog.setFixedSize(500, 600)
        dialog.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        # Nhập ID Nhân viên
        label_id = QLabel("Mã NV:")
        input_id = QLineEdit()
        layout.addWidget(label_id)
        layout.addWidget(input_id)

        # Nhập Tên Nhân viên
        label_name = QLabel("Tên NV:")
        input_name = QLineEdit()
        layout.addWidget(label_name)
        layout.addWidget(input_name)

        # Chọn ngày bắt đầu
        btn_start_date = QPushButton("Chọn Ngày Bắt Đầu")
        label_start_date = QLabel("--/--/----")
        layout.addWidget(QLabel("Ngày Bắt Đầu:"))
        layout.addWidget(btn_start_date)
        layout.addWidget(label_start_date)

        # Chọn ngày kết thúc
        btn_end_date = QPushButton("Chọn Ngày Kết Thúc")
        label_end_date = QLabel("--/--/----")
        layout.addWidget(QLabel("Ngày Kết Thúc:"))
        layout.addWidget(btn_end_date)
        layout.addWidget(label_end_date)

        # Tạo bảng lịch làm việc
        shifts = ["Sáng", "Trưa", "Chiều", "Tối"]
        days = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
        table_schedule = QTableWidget(len(shifts), len(days))
        table_schedule.setVerticalHeaderLabels(shifts)
        table_schedule.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_schedule.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Thêm checkbox vào bảng
        for i in range(len(shifts)):
            for j in range(len(days)):
                cell_widget = QWidget()
                layout_hbox = QHBoxLayout(cell_widget)
                checkbox = QCheckBox()
                layout_hbox.addWidget(checkbox)
                layout_hbox.setAlignment(Qt.AlignCenter)
                layout_hbox.setContentsMargins(0, 0, 0, 0)
                cell_widget.setLayout(layout_hbox)
                table_schedule.setCellWidget(i, j, cell_widget)

        layout.addWidget(table_schedule)

        # Nút Lưu & Hủy
        btn_layout = QHBoxLayout()
        btn_confirm = QPushButton("Lưu Lịch")
        btn_cancel = QPushButton("Hủy")
        btn_layout.addWidget(btn_confirm)
        btn_layout.addWidget(btn_cancel)
        layout.addLayout(btn_layout)

        table_schedule.setStyleSheet("background-color: white; gridline-color: black;")
        input_id.setStyleSheet("background-color: white;")
        input_name.setStyleSheet("background-color: white;")
        label_start_date.setStyleSheet("background-color: white;")
        label_end_date.setStyleSheet("background-color: white;")

        dialog.setLayout(layout)

        # ----- Xử lý chọn ngày -----
        def choose_date(label, is_start):
            """Mở lịch chọn ngày"""
            calendar_dialog = QDialog(dialog)
            calendar_dialog.setWindowTitle("Chọn Ngày")
            calendar_dialog.setFixedSize(300, 250)

            vbox = QVBoxLayout()
            calendar = QCalendarWidget()
            btn_ok = QPushButton("Chọn")

            vbox.addWidget(calendar)
            vbox.addWidget(btn_ok)
            calendar_dialog.setLayout(vbox)

            def set_date():
                selected_date = calendar.selectedDate()
                date_str = selected_date.toString("yyyy-MM-dd")
                label.setText(selected_date.toString("dd/MM/yyyy"))
                if is_start:
                    global start_date_str
                    start_date_str = date_str
                else:
                    global end_date_str
                    end_date_str = date_str
                update_table_headers()
                calendar_dialog.accept()

            btn_ok.clicked.connect(set_date)
            calendar_dialog.exec_()

        btn_start_date.clicked.connect(lambda: choose_date(label_start_date, True))
        btn_end_date.clicked.connect(lambda: choose_date(label_end_date, False))

        # ----- Cập nhật header của bảng -----
        def update_table_headers():
            """Cập nhật tiêu đề của QTableWidget (Thứ + Ngày)"""
            if "start_date_str" in globals() and start_date_str:
                start_date = QDate.fromString(start_date_str, "yyyy-MM-dd")
                for i in range(len(days)):
                    current_date = start_date.addDays(i)
                    table_schedule.setHorizontalHeaderItem(i, QTableWidgetItem(
                        f"{days[i]}\n{current_date.toString('dd/MM')}"))

        # Xử lý lưu dữ liệu
        def save_schedule():
            """Lưu lịch làm việc vào file Excel"""
            import pandas as pd
            import os

            employee_id = input_id.text().strip()
            employee_name = input_name.text().strip()

            if not employee_id or not employee_name:
                QMessageBox.warning(dialog, "Lỗi", "Vui lòng nhập đầy đủ Mã NV và Tên NV!")
                return

            if "start_date_str" not in globals() or "end_date_str" not in globals():
                QMessageBox.warning(dialog, "Lỗi", "Vui lòng chọn ngày bắt đầu và ngày kết thúc!")
                return

            file_path = f"../datasets/Schedule ({start_date_str}).xlsx"

            # Kiểm tra file có tồn tại hay không
            if os.path.exists(file_path):
                with pd.ExcelFile(file_path) as xls:
                    sheets = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in xls.sheet_names}
            else:
                sheets = {}

            # Cập nhật dữ liệu từ checkbox
            has_data = False  # Biến kiểm tra xem có dữ liệu không

            for j in range(len(days)):
                date_of_day = QDate.fromString(start_date_str, "yyyy-MM-dd").addDays(j).toString("dd-MM")
                sheet_name = f"{days[j]} - {date_of_day}"

                shifts_worked = []
                for i in range(len(shifts)):
                    cell = table_schedule.cellWidget(i, j)
                    checkbox = cell.findChild(QCheckBox) if cell else None
                    shifts_worked.append("X" if checkbox and checkbox.isChecked() else "")

                if any(shifts_worked):  # Chỉ lưu nếu có ca làm
                    has_data = True  # Đánh dấu có dữ liệu để lưu
                    if sheet_name in sheets:
                        df = sheets[sheet_name]
                    else:
                        df = pd.DataFrame(columns=["ID Nhân Viên", "Tên Nhân Viên", "Sáng", "Trưa", "Chiều", "Tối"])

                    existing_entry = df[df["ID Nhân Viên"] == employee_id]
                    if not existing_entry.empty:
                        index = existing_entry.index[0]
                        df.loc[index, "Sáng":"Tối"] = shifts_worked
                    else:
                        df.loc[len(df)] = [employee_id, employee_name] + shifts_worked

                    sheets[sheet_name] = df

                    # Kiểm tra dữ liệu trước khi ghi
                    print(f"📌 Dữ liệu sheet {sheet_name}:")
                    print(df)

            if not has_data:
                QMessageBox.warning(dialog, "Lỗi", "Không có dữ liệu ca làm nào được chọn!")
                return

            # Ghi lại vào file Excel
            try:
                with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
                    for sheet_name, df in sheets.items():
                        df.to_excel(writer, sheet_name=sheet_name, index=False)

                QMessageBox.information(dialog, "Thành công", f"Lịch làm việc đã được lưu vào {file_path}!")
                print(f"✅ File đã được lưu: {file_path}")
                dialog.close()
            except Exception as e:
                self.show_warning(f"Lỗi khi lưu file: {str(e)}")
                print(f"❌ Lỗi khi lưu file: {str(e)}")

        btn_confirm.clicked.connect(save_schedule)
        btn_cancel.clicked.connect(dialog.close)
        dialog.exec_()

    def delete_employee(self):
        """Xóa nhân viên được chọn khỏi bảng và JSON"""
        selected_row = self.tableWidgetEmployee.currentRow()
        if selected_row == -1:
            self.show_warning("Vui lòng chọn một nhân viên để xóa!")
            return

        reply = self.show_question("Bạn có chắc chắn muốn xóa nhân viên này?")

        if reply == QMessageBox.StandardButton.Yes:
            # Lấy ID của nhân viên từ bảng
            employee_id = self.tableWidgetEmployee.item(selected_row, 0).text()

            # Đọc danh sách nhân viên từ JSON
            employees = self.dc.get_all_employees()
            if employees is None:
                employees = []

            # Lọc danh sách nhân viên để loại bỏ nhân viên có ID trùng khớp
            employees = [emp for emp in employees if emp.id != employee_id]

            # Lưu lại danh sách mới vào JSON
            try:
                jff = JsonFileFactory()
                filename = "../datasets/employees.json"
                jff.write_data(employees, filename)
            except Exception as e:
                self.show_warning(f"Lỗi khi lưu file JSON: {str(e)}")
                return

            # Xóa dòng khỏi bảng
            self.tableWidgetEmployee.removeRow(selected_row)

            self.show_information(" Nhân viên đã được xóa!")

    def fill_table_widget(self, data):
        self.tableWidgetChamCong.setRowCount(len(data))
        self.tableWidgetChamCong.setColumnCount(len(data.columns))
        self.tableWidgetChamCong.setHorizontalHeaderLabels(data.columns)

        for row_idx, row_data in data.iterrows():
            for col_idx, value in enumerate(row_data):
                self.tableWidgetChamCong.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def load_attendance_data(self):
        """ Chọn file Excel, đọc dữ liệu, và hiển thị lên tableWidgetChamCong """
        file_path, _ = QFileDialog.getOpenFileName(
            self.MainWindow,
            "Chọn file Excel chấm công",
            "",
            "Excel Files (*.xlsx *.xls)"
        )

        if not file_path:
            return

        # Đọc file Excel
        xls = pd.ExcelFile(file_path)
        print(f"Đọc file: {file_path}, các sheet: {xls.sheet_names}")

        # Xác định các cột ngày/thứ từ tên sheet
        sheet_columns = xls.sheet_names  # Mỗi sheet là một ngày -> Dùng làm tiêu đề cột

        # Danh sách lưu thông tin chấm công
        data_list = []

        # Duyệt từng sheet để lấy dữ liệu
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)

            # Kiểm tra xem file có đủ cột không
            required_columns = ["ID Nhân Viên", "Tên Nhân Viên"]
            for col in required_columns:
                if col not in df.columns:
                    print(f"Lỗi: Cột {col} không tồn tại trong sheet {sheet_name}")
                    return

            # Duyệt từng nhân viên
            for _, row in df.iterrows():
                id_nv = row["ID Nhân Viên"]
                ten_nv = row["Tên Nhân Viên"]

                # Luôn tạo đủ 4 dòng cho mỗi nhân viên (Sáng, Trưa, Chiều, Tối)
                for ca in ["Sáng", "Trưa", "Chiều", "Tối"]:
                    data_list.append([id_nv, ten_nv, ca] + [""] * len(sheet_columns))  # Cột ngày/thứ để trống

        # Hiển thị dữ liệu lên tableWidgetChamCong
        self.tableWidgetChamCong.setRowCount(len(data_list))
        self.tableWidgetChamCong.setColumnCount(3 + len(sheet_columns))  # 3 cột (ID, Tên, Ca) + cột ngày/thứ

        # Thiết lập tiêu đề cột
        headers = ["ID Nhân Viên", "Tên Nhân Viên", "Ca"] + sheet_columns  # Lấy tên sheet làm tiêu đề cột
        self.tableWidgetChamCong.setHorizontalHeaderLabels(headers)

        # Điền dữ liệu vào bảng
        for row_idx, row_data in enumerate(data_list):
            for col_idx, value in enumerate(row_data):
                self.tableWidgetChamCong.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        print("Dữ liệu đã được load thành công vào bảng!")

    def update_attendance_status(self, row, column):
        if column < 3:  # Chặn đổi màu ở 3 cột đầu tiên
            return

        item = self.tableWidgetChamCong.item(row, column)
        if item is None:
            item = QTableWidgetItem()
            self.tableWidgetChamCong.setItem(row, column, item)

        # Danh sách màu theo trạng thái
        colors = ["#FFFFFF", "#00FF00", "#FFFF00", "#FF0000"]  # Trắng, Xanh lá, Vàng, Đỏ

        # Lấy màu hiện tại (nếu ô chưa có màu, đặt mặc định là trắng)
        current_color = item.background().color().name().upper()

        # Debug: In ra màu hiện tại để kiểm tra
        print(f"Row {row}, Column {column}, Current Color: {current_color}")

        # Kiểm tra nếu màu hiện tại không có trong danh sách, gán mặc định là trắng
        if current_color not in colors:
            current_color = colors[0]  # Trắng

        # Xác định màu tiếp theo
        next_index = (colors.index(current_color) + 1) % len(colors)
        next_color = colors[next_index]

        # Đổi màu
        item.setBackground(QColor(next_color))

        # Debug: In màu tiếp theo để kiểm tra
        print(f"Next Color: {next_color}")

    def save_attendance_to_excel(self):
        """Lưu dữ liệu bảng chấm công vào file Excel, không bị lặp nhân viên."""

        # Hộp thoại chọn file import trước đó
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Chọn file Excel đã import",
            dir="",
            filter="Excel Files (*.xlsx *.xls)"
        )

        if not file_path:
            print("❌ Không có file nào được chọn.")
            return

        # Lấy tên file gốc để đặt tên file lưu
        file_name = os.path.basename(file_path)
        file_name = file_name.replace("Schedule", "Check_schedule")
        save_path = os.path.join("../datasets", file_name)

        if not save_path.endswith(".xlsx"):
            save_path += ".xlsx"

        # Lấy dữ liệu từ bảng
        rows = self.tableWidgetChamCong.rowCount()
        cols = self.tableWidgetChamCong.columnCount()

        headers = ["ID Nhân Viên", "Tên Nhân Viên", "Ca"] + \
                  [self.tableWidgetChamCong.horizontalHeaderItem(i).text() for i in range(3, cols)]

        color_map = {
            "#FFFFFF": "",
            "#00FF00": "Đi làm",
            "#FFFF00": "Nghỉ có phép",
            "#FF0000": "Nghỉ không phép"
        }

        data = []
        seen_ids = set()  # Tránh lặp nhân viên

        for row in range(0, rows, 4):
            id_nv = self.tableWidgetChamCong.item(row, 0).text() if self.tableWidgetChamCong.item(row, 0) else ""
            ten_nv = self.tableWidgetChamCong.item(row, 1).text() if self.tableWidgetChamCong.item(row, 1) else ""

            # Kiểm tra nếu ID đã được ghi thì bỏ qua (tránh ghi lại nhân viên)
            if id_nv in seen_ids:
                continue
            seen_ids.add(id_nv)

            for i, ca in enumerate(["Sáng", "Trưa", "Chiều", "Tối"]):
                row_data = [id_nv, ten_nv, ca]
                for col in range(3, cols):
                    item = self.tableWidgetChamCong.item(row + i, col)
                    if item:
                        cell_color = item.background().color().name().upper()
                        cell_value = color_map.get(cell_color, "")
                        row_data.append(cell_value)
                    else:
                        row_data.append("")
                data.append(row_data)

        df = pd.DataFrame(data, columns=headers)
        df.to_excel(save_path, index=False, engine='openpyxl')

        print(f"✅ Đã lưu file chấm công tại: {save_path}")

############################################################################
######################## Quản lý doanh thu ###3#############################
    def show_chart_by_month(self):
        try:
            excel_path = "../datasets/doanh_thu_theo_thang.xlsx"
            df = pd.read_excel(excel_path)

            if df.empty:
                print("Dữ liệu tháng rỗng.")
                return

            df["Tháng/Năm"] = df["Tháng/Năm"].astype(str)
            df = df.sort_values(by="Tháng/Năm")

            if not self.frame_bieudo1.layout():
                self.frame_bieudo1.setLayout(QVBoxLayout())

            layout = self.frame_bieudo1.layout()
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            fig, ax = plt.subplots(figsize=(10, 5), facecolor="#f8f9fa")
            bars = ax.bar(df["Tháng/Năm"], df["Tổng doanh thu (VNĐ)"],
                          color="#5A67D8", width=0.6)

            ax.set_title("🔵 Doanh thu theo tháng", fontsize=14, fontweight='bold', color="#333")
            ax.set_xlabel("Tháng/Năm", fontsize=12, color="#555")
            ax.set_ylabel("Tổng doanh thu (VNĐ)", fontsize=12, color="#555")
            ax.tick_params(axis='x', rotation=45, labelsize=10)
            ax.tick_params(axis='y', labelsize=10)
            ax.grid(axis="y", linestyle="--", alpha=0.5)

            # Hiển thị giá trị trên từng cột
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f"{height:,.0f}",
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 5), textcoords="offset points",
                            ha='center', fontsize=9, color="#333")

            canvas = FigureCanvas(fig)
            layout.addWidget(canvas)

        except Exception as e:
            print(f"Lỗi khi vẽ biểu đồ tháng: {e}")

    def show_chart_by_week(self):
        try:
            excel_path = "../datasets/doanh_thu_theo_tuan_chuan.xlsx"
            df = pd.read_excel(excel_path)

            if df.empty:
                print("Dữ liệu tuần rỗng.")
                return

            df["Tuần/Tháng/Năm"] = df["Tuần/Tháng/Năm"].astype(str)
            df = df.sort_values(by="Tuần/Tháng/Năm")

            if not self.frame_bieudo.layout():
                self.frame_bieudo.setLayout(QVBoxLayout())

            layout = self.frame_bieudo.layout()
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            fig, ax = plt.subplots(figsize=(12, 5), facecolor="#f8f9fa")
            ax.plot(df["Tuần/Tháng/Năm"], df["Tổng doanh thu (VNĐ)"],
                    color="#E76F51", marker='o', linewidth=2)

            ax.set_title("🟠 Doanh thu theo tuần (trong từng tháng)", fontsize=14,
                         fontweight='bold', color="#333")
            ax.set_xlabel("Tuần/Tháng/Năm", fontsize=12, color="#555")
            ax.set_ylabel("Tổng doanh thu (VNĐ)", fontsize=12, color="#555")
            ax.tick_params(axis='x', rotation=45, labelsize=10)
            ax.tick_params(axis='y', labelsize=10)
            ax.grid(axis="y", linestyle="--", alpha=0.5)

            # Hiển thị giá trị trên từng điểm
            for i, value in enumerate(df["Tổng doanh thu (VNĐ)"]):
                ax.annotate(f"{value:,.0f}", (i, value),
                            textcoords="offset points", xytext=(0, 5),
                            ha='center', fontsize=9, color="#333")

            canvas = FigureCanvas(fig)
            layout.addWidget(canvas)

        except Exception as e:
            print(f"Lỗi khi vẽ biểu đồ tuần: {e}")

    def display_total_customers(self):
        """ Đọc dữ liệu và hiển thị tổng khách hàng lên frameCustomer """
        try:
            # Đọc dữ liệu từ file JSON
            with open("../datasets/customers.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            total_customers = len(data)

            # --- Layout chính ---
            main_layout = QHBoxLayout()
            main_layout.setContentsMargins(0, 0, 0, 0)
            main_layout.setSpacing(0)

            # --- Thanh màu xanh bên trái ---
            left_bar = QFrame()
            left_bar.setFixedWidth(10)
            left_bar.setStyleSheet(
                "background-color: #4A90E2; border-top-left-radius: 16px; border-bottom-left-radius: 16px;")

            # --- Layout phần chữ ---
            text_layout = QVBoxLayout()
            text_layout.setContentsMargins(16, 16, 16, 16)
            text_layout.setSpacing(10)

            title_label = QLabel("Customers")
            title_label.setFont(QFont("Segoe UI", 15, QFont.Normal))
            title_label.setStyleSheet("color: #000000;")

            number_label = QLabel(f"{total_customers:,}")
            number_label.setFont(QFont("Segoe UI", 25, QFont.Bold))
            number_label.setStyleSheet("color: #000000;")

            text_layout.addWidget(title_label)
            text_layout.addWidget(number_label)
            text_layout.addStretch()

            text_container = QWidget()
            text_container.setLayout(text_layout)

            # --- Icon khách hàng bên phải ---
            icon_label = QLabel()
            icon_label.setFixedSize(50, 50)
            icon_label.setPixmap(
                QPixmap("../images/customer_icon.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_label.setAlignment(Qt.AlignCenter)

            # --- Thêm vào layout chính ---
            main_layout.addWidget(left_bar)
            main_layout.addWidget(text_container, 1)
            main_layout.addWidget(icon_label)

            # --- Xóa layout cũ nếu có ---
            if self.frameCustomer.layout():
                old_layout = self.frameCustomer.layout()
                while old_layout.count():
                    child = old_layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            self.frameCustomer.setLayout(main_layout)

            # --- Style: bo góc, nền trong suốt, không viền ---
            self.frameCustomer.setStyleSheet("""
                QFrame {
                    background-color: transparent;
                    border-radius: 16px;
                    border: none;
                }
                QLabel {
                    background: transparent;
                }
            """)

        except Exception as e:
            print("❌ Lỗi khi đọc dữ liệu khách hàng:", e)

    def bill(self):
        """ Đọc dữ liệu và hiển thị tổng khách hàng lên frameInvoice """
        try:
            # Đọc dữ liệu từ file JSON
            with open("../datasets/customers.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            total_customers = len(data)

            # --- Layout chính ---
            main_layout = QHBoxLayout()
            main_layout.setContentsMargins(0, 0, 0, 0)
            main_layout.setSpacing(0)

            # --- Thanh màu xanh bên trái ---
            left_bar = QFrame()
            left_bar.setFixedWidth(10)
            left_bar.setStyleSheet(
                "background-color: #4A90E2; border-top-left-radius: 16px; border-bottom-left-radius: 16px;")

            # --- Layout phần chữ ---
            text_layout = QVBoxLayout()
            text_layout.setContentsMargins(16, 16, 16, 16)
            text_layout.setSpacing(4)

            title_label = QLabel("Invoices")
            title_label.setFont(QFont("Segoe UI", 15, QFont.Normal))
            title_label.setStyleSheet("color: #000000;")

            number_label = QLabel(f"{total_customers:,}")
            number_label.setFont(QFont("Segoe UI", 25, QFont.Bold))
            number_label.setStyleSheet("color: #000000;")

            text_layout.addWidget(title_label)
            text_layout.addWidget(number_label)
            text_layout.addStretch()

            text_container = QWidget()
            text_container.setLayout(text_layout)

            # --- Icon khách hàng bên phải ---
            icon_label = QLabel()
            icon_label.setFixedSize(40, 40)
            icon_label.setPixmap(
                QPixmap("../images/bill_icon.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_label.setAlignment(Qt.AlignCenter)

            # --- Thêm vào layout chính ---
            main_layout.addWidget(left_bar)
            main_layout.addWidget(text_container, 1)
            main_layout.addWidget(icon_label)

            # --- Xóa layout cũ nếu có ---
            if self.frameInvoices.layout():
                old_layout = self.frameInvoices.layout()
                while old_layout.count():
                    child = old_layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            self.frameInvoices.setLayout(main_layout)

            # --- Style: bo góc, nền trong suốt, không viền ---
            self.frameInvoices.setStyleSheet("""
                QFrame {
                    background-color: transparent;
                    border-radius: 16px;
                    border: none;
                }
                QLabel {
                    background: transparent;
                }
            """)

        except Exception as e:
            print("❌ Lỗi khi đọc dữ liệu khách hàng:", e)

    def display_total_revenue(self):
        """ Đọc dữ liệu và hiển thị tổng doanh thu lên frameRevenue """
        try:
            # Đọc dữ liệu từ file JSON
            with open("../datasets/customers.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            # Tính tổng doanh thu
            total_revenue = sum(customer.get("total_payment", 0) for customer in data)

            # --- Layout chính ---
            main_layout = QHBoxLayout()
            main_layout.setContentsMargins(0, 0, 0, 0)
            main_layout.setSpacing(0)

            # --- Thanh màu xanh bên trái ---
            left_bar = QFrame()
            left_bar.setFixedWidth(10)
            left_bar.setStyleSheet(
                "background-color: #4A90E2; border-top-left-radius: 16px; border-bottom-left-radius: 16px;")

            # --- Layout phần chữ ---
            text_layout = QVBoxLayout()
            text_layout.setContentsMargins(16, 16, 16, 16)
            text_layout.setSpacing(4)

            title_label = QLabel("Total Revenue")
            title_label.setFont(QFont("Segoe UI", 15, QFont.Normal))
            title_label.setStyleSheet("color: #000000;")

            number_label = QLabel(f"{total_revenue:,.0f} VND")
            number_label.setFont(QFont("Segoe UI", 25, QFont.Bold))
            number_label.setStyleSheet("color: #000000;")

            text_layout.addWidget(title_label)
            text_layout.addWidget(number_label)
            text_layout.addStretch()

            text_container = QWidget()
            text_container.setLayout(text_layout)

            # --- Icon tiền bên phải ---
            icon_label = QLabel()
            icon_label.setFixedSize(40, 40)
            icon_label.setPixmap(
                QPixmap("../images/revenue_icon.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_label.setAlignment(Qt.AlignCenter)

            # --- Thêm vào layout chính ---
            main_layout.addWidget(left_bar)
            main_layout.addWidget(text_container, 1)
            main_layout.addWidget(icon_label)

            # --- Xóa layout cũ nếu có ---
            if self.frameRevenue.layout():
                old_layout = self.frameRevenue.layout()
                while old_layout.count():
                    child = old_layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            self.frameRevenue.setLayout(main_layout)

            # --- Style: bo góc, nền trong suốt, không viền ---
            self.frameRevenue.setStyleSheet("""
                QFrame {
                    background-color: transparent;
                    border-radius: 16px;
                    border: none;
                }
                QLabel {
                    background: transparent;
                }
            """)

        except Exception as e:
            print("❌ Lỗi khi đọc dữ liệu doanh thu:", e)

    def load_bieudo(self):
        if not self.frame_bieudo1.layout():
            self.frame_bieudo1.setLayout(QVBoxLayout())














