import pandas as pd
import matplotlib.pyplot as plt

# === Đọc dữ liệu từ 2 file Excel ===
df_month = pd.read_excel("../datasets/doanh_thu_theo_thang.xlsx")
df_week = pd.read_excel("../datasets/doanh_thu_theo_tuan_chuan.xlsx")

df_month = df_month.sort_values(by="Tháng/Năm")
df_week = df_week.sort_values(by="Tuần/Tháng/Năm")

# ===========================
# 🔷 Biểu đồ cột: Theo THÁNG
# ===========================
plt.figure(figsize=(10, 5), facecolor="#f8f9fa")
bars = plt.bar(df_month["Tháng/Năm"], df_month["Tổng doanh thu (VNĐ)"],
               color="#5A67D8", width=0.6)

plt.title("🔵 Doanh thu theo tháng", fontsize=14, fontweight='bold', color="#333")
plt.xlabel("Tháng/Năm", fontsize=12, color="#555")
plt.ylabel("Tổng doanh thu (VNĐ)", fontsize=12, color="#555")
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Hiển thị giá trị trên từng cột
for bar in bars:
    height = bar.get_height()
    plt.annotate(f"{height:,.0f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5), textcoords="offset points",
                 ha='center', fontsize=9, color="#333")

plt.tight_layout()
plt.show()

# ============================
# 🟠 Biểu đồ đường: Theo TUẦN
# ============================
plt.figure(figsize=(12, 5), facecolor="#f8f9fa")
plt.plot(df_week["Tuần/Tháng/Năm"], df_week["Tổng doanh thu (VNĐ)"],
         color="#E76F51", marker='o', linewidth=2)

plt.title("🟠 Doanh thu theo tuần (trong từng tháng)", fontsize=14, fontweight='bold', color="#333")
plt.xlabel("Tuần/Tháng/Năm", fontsize=12, color="#555")
plt.ylabel("Tổng doanh thu (VNĐ)", fontsize=12, color="#555")
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Hiển thị giá trị trên từng điểm
for i, value in enumerate(df_week["Tổng doanh thu (VNĐ)"]):
    plt.annotate(f"{value:,.0f}", (i, value), textcoords="offset points",
                 xytext=(0, 5), ha='center', fontsize=9, color="#333")

plt.tight_layout()
plt.show()
