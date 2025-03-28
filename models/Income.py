import json
import math
import pandas as pd
from datetime import datetime
import os

# ======= BƯỚC 1: Đọc dữ liệu từ JSON =======
with open('../datasets/customers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ======= Hàm chuẩn hóa ngày giờ =======
def parse_datetime(x):
    formats = ["%d/%m/%Y %H:%M", "%H:%M %d/%m/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(x, fmt)
        except ValueError:
            continue
    return None

df['last_transaction_time'] = df['last_transaction_time'].apply(parse_datetime)
df.dropna(subset=['last_transaction_time'], inplace=True)

# Tách ngày - tháng - năm
df['Ngày'] = df['last_transaction_time'].dt.day
df['Tháng'] = df['last_transaction_time'].dt.month
df['Năm'] = df['last_transaction_time'].dt.year

# Tạo thư mục lưu file nếu chưa có
excel_folder = "../datasets"
os.makedirs(excel_folder, exist_ok=True)

# ================================
# ✅ PHẦN 1: DOANH THU THEO THÁNG
# ================================
df['Tháng/Năm'] = df['last_transaction_time'].dt.strftime('%m/%Y')

doanh_thu_thang = df.groupby('Tháng/Năm')['total_payment'].sum().reset_index()
doanh_thu_thang.columns = ['Tháng/Năm', 'Tổng doanh thu (VNĐ)']

# Xuất file Excel doanh thu theo tháng
excel_thang_path = os.path.join(excel_folder, "doanh_thu_theo_thang.xlsx")
doanh_thu_thang.to_excel(excel_thang_path, index=False)
print(f"✅ Đã xuất file: {excel_thang_path}")

# ===============================
# ✅ PHẦN 2: DOANH THU THEO TUẦN
# ===============================
# Tính tuần trong tháng (mỗi tuần là 7 ngày)
df['Tuần'] = df['Ngày'].apply(lambda d: math.ceil(d / 7))

# Nhóm theo Năm - Tháng - Tuần
doanh_thu_tuan = df.groupby(['Năm', 'Tháng', 'Tuần'])['total_payment'].sum().reset_index()

# Tạo cột hiển thị: "Tuần x - mm/yyyy"
doanh_thu_tuan['Tuần/Tháng/Năm'] = (
    'Tuần ' + doanh_thu_tuan['Tuần'].astype(str) +
    ' - ' + doanh_thu_tuan['Tháng'].astype(str).str.zfill(2) +
    '/' + doanh_thu_tuan['Năm'].astype(str)
)

# Sắp xếp đúng thứ tự
doanh_thu_tuan = doanh_thu_tuan.sort_values(by=['Năm', 'Tháng', 'Tuần'])

# Đổi tên cột
doanh_thu_tuan = doanh_thu_tuan[['Tuần/Tháng/Năm', 'total_payment']]
doanh_thu_tuan.columns = ['Tuần/Tháng/Năm', 'Tổng doanh thu (VNĐ)']

# Xuất file Excel doanh thu theo tuần
excel_tuan_path = os.path.join(excel_folder, "doanh_thu_theo_tuan_chuan.xlsx")
doanh_thu_tuan.to_excel(excel_tuan_path, index=False)
print(f"✅ Đã xuất file: {excel_tuan_path}")