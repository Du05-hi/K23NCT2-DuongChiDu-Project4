from database import engine

try:
    # Thử mở một kết nối đến SQL Server
    with engine.connect() as connection:
        print("========================================")
        print("🎉 KẾT NỐI DATABASE THÀNH CÔNG!")
        print("Cấu hình SQLAlchemy của cậu đã hoạt động chuẩn xác.")
        print("========================================")
except Exception as e:
    print("========================================")
    print("❌ KẾT NỐI THẤT BẠI. Cậu xem lỗi chi tiết ở dưới nhé:")
    print(e)
    print("========================================")