from database import SessionLocal
from models import User, Category, Course

def seed_db():
    db = SessionLocal()
    try:
        print("Đang kiểm tra và thêm dữ liệu mẫu...")
        
        # 1. Tạo tài khoản Admin
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            admin = User(
                username="admin", 
                password="123456", 
                full_name="Nguyễn Mạnh Tuấn", 
                role="admin"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print("- Đã tạo tài khoản Admin")

        # 2. Tạo Danh mục khóa học
        if db.query(Category).count() == 0:
            cat1 = Category(name="Lập trình Web & Backend")
            cat2 = Category(name="Vật lý & Khoa học")
            db.add_all([cat1, cat2])
            db.commit()
            print("- Đã tạo 2 danh mục học tập")

            # 3. Tạo Khóa học mẫu
            course1 = Course(
                category_id=cat1.id, 
                instructor_id=admin.id, 
                title="Xây dựng hệ thống LMS với Python Flask & SQL Server", 
                price=500000, 
                status="published"
            )
            course2 = Course(
                category_id=cat2.id, 
                instructor_id=admin.id, 
                title="Mô phỏng Nhiệt động lực học trực quan với Crocodile Physics", 
                price=450000, 
                status="published"
            )
            db.add_all([course1, course2])
            db.commit()
            print("- Đã tạo 2 khóa học mẫu")
        else:
            print("- Dữ liệu đã tồn tại, không cần thêm mới.")

        print("🎉 HOÀN TẤT! Cậu có thể bật app.py lên để test giao diện được rồi!")

    except Exception as e:
        print("❌ Lỗi trong quá trình thêm dữ liệu:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()