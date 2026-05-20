
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text, DateTime, Date, NVARCHAR, Numeric
from database import Base
from sqlalchemy.ext.declarative import declarative_base
import datetime
                
Base = declarative_base()
# ==========================================
# 1. NGƯỜI DÙNG & HỆ THỐNG
# ==========================================
class User(Base):
    __tablename__ = "g10users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50))
    is_active = Column(Boolean, default=True)

class Notification(Base):
    __tablename__ = "g10notifications"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(String(500), nullable=False)
    is_read = Column(Boolean, default=False)

# ==========================================
# 2. KHÓA HỌC & BÀI HỌC
# ==========================================
class Category(Base):
    __tablename__ = "g10categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('g10categories.id'), nullable=True)

class Course(Base):
    __tablename__ = "g10courses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('g10categories.id'), nullable=False)
    instructor_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    price = Column(Numeric(18, 2), nullable=False) 
    status = Column(String(50))

class Section(Base):
    __tablename__ = "g10sections"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    title = Column(String(255), nullable=False)
    order_index = Column(Integer, nullable=False)

class Lesson(Base):
    __tablename__ = "g10lessons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    section_id = Column(Integer, ForeignKey('g10sections.id'), nullable=False)
    lesson_type = Column(String(50))
    url_content = Column(String(500))

# ==========================================
# 3. THI CỬ & TRẮC NGHIỆM
# ==========================================
class Quiz(Base):
    __tablename__ = "g10quizzes"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=True)
    time_limit = Column(Integer, nullable=False)
    pass_score = Column(Float, nullable=False)
    difficulty = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False) 

class Question(Base):
    __tablename__ = "g10questions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey('g10quizzes.id'), nullable=False)
    content = Column(String(500), nullable=False)
    point = Column(Float, nullable=False)

class Option(Base):
    __tablename__ = "g10options"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('g10questions.id'), nullable=False)
    option_text = Column(String(255), nullable=False)
    is_correct = Column(Boolean, nullable=False)

# ==========================================
# 4. TIẾN ĐỘ & KẾT QUẢ
# ==========================================
class Enrollment(Base):
    __tablename__ = "g10enrollments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    enrolled_at = Column(DateTime, default=datetime.datetime.now)
    status = Column(String(50))

class CourseProgress(Base):
    __tablename__ = "g10course_progress"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    lesson_id = Column(Integer, ForeignKey('g10lessons.id'), nullable=False)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime)

class QuizResult(Base):
    __tablename__ = "g10quiz_results"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('g10quizzes.id'), nullable=False)
    total_score = Column(Float, nullable=False)
    status = Column(String(50))
    attempt_count = Column(Integer)

# ==========================================
# 5. TÀI CHÍNH & TƯƠNG TÁC
# ==========================================
class Payment(Base):
    __tablename__ = "g10payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    amount = Column(Numeric(18, 2), nullable=False) 
    payment_method = Column(String(100), nullable=False)
    transaction_id = Column(String(100), nullable=False)
   

class Coupon(Base):
    __tablename__ = "g10coupons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), nullable=False)
    discount_val = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    usage_limit = Column(Integer, nullable=False)

class Review(Base):
    __tablename__ = "g10reviews"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    rating = Column(Integer)
    comment = Column(String(500))
    created_at = Column(DateTime)



class Assignment(Base):
    __tablename__ = "g10assignments"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)
    question = Column(String)
    answer = Column(String)

class Attendance(Base):
    __tablename__ = "g10attendance"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    status = Column(Boolean)
class Event(Base):
    __tablename__ = 'g10events'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(NVARCHAR(255), nullable=False)
    event_date = Column(Date, nullable=False)
    status = Column(NVARCHAR(50), nullable=False)

class Order(Base):
    __tablename__ = "g10orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    course_title = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String(50), default="Đang xác nhận")
