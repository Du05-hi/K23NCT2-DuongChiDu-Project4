from database import engine, Base
import models  # Bắt buộc phải import models để SQLAlchemy nhận diện được 15 class bảng

print("Đang tiến hành tạo 15 bảng vào SQL Server...")
# Lệnh này sẽ kết nối DB và tự động tạo toàn bộ bảng chưa tồn tại
Base.metadata.create_all(bind=engine)
print("Thành công! Mở SQL Server lên kiểm tra thôi cậu!")