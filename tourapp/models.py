from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from tourapp import db, app
from datetime import datetime
from flask_login import UserMixin
from enum import Enum as UserEnum


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

#dky
class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

#dky
class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    Bill = relationship('Bill', backref='user', lazy=False)

    def __str__(self):
        return self.name


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(255), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(255), nullable=False)
    time = Column(String(255))
    price_big = Column(Float, default=0)
    price_small = Column(Float, default=0)
    datetime_start = Column(Date, nullable=True)
    datetime_end = Column(Date)
    go_start = Column(String(100), nullable=False)
    go_end = Column(String(100), nullable=False)
    vehicle = Column(String(100), nullable=False)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    Bill = relationship('Bill', backref='product', lazy=False)

    def __str__(self):
        return self.name


class Bill(BaseModel):
    tablename = 'bill'

    name = Column(String(255))
    email = Column(String(255))
    amount_big = Column(Integer)
    amount_young = Column(Integer)
    phone = Column(Integer)
    address = Column(String(255))
    cccd = Column(Integer)
    pay_date = Column(Date)
    active = Column(Boolean, default=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    total = Column(Integer)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='MIỀN BẮC')
        # c2 = Category(name='MIỀN TRUNG')
        # c3 = Category(name='MIỀN NAM')
        #
        # db.session.add_all([c1, c2, c3])
        #
        # p1 = Product(name="DU LỊCH ĐẢO PHÚ QUỐC", time="3 ngày 3 đêm", price_big=398, price_small=241,
        #              datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Phú Quốc", vehicle="Máy bay", image="images/anh1.jpg", category_id=3)
        #
        # p2 = Product(name="DU LỊCH ĐÀ NẴNG", time="3 ngày 2 đêm", price_big=279, price_small=173,
        #              datetime_start="2023-03-09", datetime_end="2023-03-12", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Nẵng", vehicle="Máy bay", image="images/anh2.jpg",
        #              category_id=2)
        #
        # p3 = Product(name="DU LỊCH ĐÀ LẠT", time="3 ngày 2 đêm", price_big=97, price_small=67,
        #              datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Lạt", vehicle="Ôtô", image="images/anh3.png", category_id=2)
        #
        # p4 = Product(name="DU LỊCH SAPA", time="4 ngày 3 đêm", price_big=424, price_small=305,
        #              datetime_start="2023-03-10", datetime_end="2023-03-14", go_start="TP. Hồ Chí Minh",
        #              go_end="Điện Biên - SaPa", vehicle="Máy bay",
        #              image="images/anh4.jpg", category_id=1)
        #
        # p5 = Product(name="DU LỊCH NHA TRANG", time="3 ngày 2 đêm", price_big=106, price_small=67,
        #              datetime_start="2023-03-11", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Nha Trang", vehicle="Máy bay",
        #              image="images/anh5.jpg", category_id=2)
        #
        # p6 = Product(name="DU LỊCH HẠ LONG", time="2 ngày 1 đêm", price_big=206, price_small=106,
        #              datetime_start="2023-03-14", datetime_end="2023-03-17", go_start="TP. Hồ Chí Minh",
        #              go_end="Hạ Long", vehicle="Máy bay",
        #              image="images/anh6.jpg", category_id=1)
        #
        # p7 = Product(name="DU LỊCH PHÚ YÊN", time="3 ngày 3 đêm", price_big=228, price_small=161,
        #              datetime_start="2023-03-15", datetime_end="2023-03-19", go_start="TP. Hồ Chí Minh",
        #              go_end="Phú Yên - Tuy Hòa", vehicle="Máy bay",
        #              image="images/anh7.jpg", category_id=3)
        #
        # p8 = Product(name="DU LỊCH HUẾ", time="4 ngày 3 đêm", price_big=678, price_small=466,
        #              datetime_start="2023-03-15", datetime_end="2023-03-21", go_start="TP. Hồ Chí Minh",
        #              go_end="Huế", vehicle="Máy bay",
        #              image="images/anh8.jpg", category_id=2)
        #
        # p9 = Product(name="DU LỊCH TÂY NGUYÊN", time="3 ngày 2 đêm", price_big=220, price_small=156,
        #              datetime_start="2023-03-15", datetime_end="2023-03-19", go_start="TP. Hồ Chí Minh",
        #              go_end="Tây Nguyên", vehicle="Máy bay",
        #              image="images/anh9.jpg", category_id=2)
        #
        # p10 = Product(name="DU LỊCH MỸ THO", time="2 ngày 1 đêm", price_big=80, price_small=67,
        #               datetime_start="2023-03-15", datetime_end="2023-03-18", go_start="TP. Hồ Chí Minh",
        #               go_end="Mỹ Tho", vehicle="Ôtô",
        #               image="images/anh10.jpg", category_id=3)
        #
        # p11 = Product(name="DU LỊCH HỘI AN", time="4 ngày 3 đêm", price_big=212, price_small=114,
        #               datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #               go_end="Hội An - Đà Nẵng", vehicle="Máy bay",
        #               image="images/anh11.jpg", category_id=2)
        #
        # p12 = Product(name="DU LỊCH HÀ GIANG", time="4 ngày 3 đêm", price_big=339, price_small=254,
        #               datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #               go_end="Hà Giang", vehicle="Máy bay",
        #               image="images/anh12.jpg", category_id=1)
        # p13 = Product(name="DU LỊCH HÀ NỘI", time="4 ngày 3 đêm", price_big=114, price_small=106,
        #               datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #               go_end="Hà Nội", vehicle="Máy bay",
        #               image="images/anh14.jpg", category_id=1)
        # p14 = Product(name="DU LỊCH CẦN THƠ", time="2 ngày 1 đêm", price_big=106, price_small=63,
        #               datetime_start="2023-03-15", datetime_end="2023-03-18", go_start="TP. Hồ Chí Minh",
        #               go_end="Cần Thơ", vehicle="Ôtô",
        #               image="images/anh13.jpg", category_id=3)
        # p15 = Product(name="DU LỊCH BẮC NINH", time="4 ngày 3 đêm", price_big=180, price_small=152,
        #               datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #               go_end="Bắc Ninh", vehicle="Máy bay",
        #               image="images/anh15.jpg", category_id=1)
        # db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15])
        # db.session.commit()
        #
        #
        u1 = User(name='Hoàng', username='hoang', password='202cb962ac59075b964b07152d234b70', email='20172023218@gmail.com')
        u2 = User(name='Thái Tấn Phát', username='phat', password='202cb962ac59075b964b07152d234b70',email='phattan@ou.edu.vn')
        u3 = User(name='Lê Văn Lâm', username='lam', password='202cb962ac59075b964b07152d234b70',email='levanlam@ou.edu.vn')
        u4 = User(name='Nguyễn Thị Ngọc Yến', username='yen', password='202cb962ac59075b964b07152d234b70',email='ngocyennguyen@ou.edu.vn')
        u5 = User(name='Nguyễn Thị Thanh', username='thanh', password='202cb962ac59075b964b07152d234b70',email='thanhjenny@ou.edu.vn')
        u6 = User(name='Phan Thị Yến Vi', username='vi', password='202cb962ac59075b964b07152d234b70',email='yenviphan@ou.edu.vn')
        u7 = User(name='Nguyễn Toàn Mỹ', username='my', password='202cb962ac59075b964b07152d234b70',email='mynguyen@ou.edu.vn')
        u8 = User(name='Admin', username='admin', password='202cb962ac59075b964b07152d234b70', email='admin@ou.edu.vn', user_role='ADMIN')
        db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8])
        db.session.commit()


        b1 = Bill(name="Minh Hoàng", email="2011172018@gmail.com", amount_big=2, amount_young=1, phone="0364121547",
                  address="635 Phan Văn Trị, P7, Gò Vấp, Thành Phố Hồ Chí Minh", cccd="231417171", pay_date="2023-02-20", total=452, product_id=2, user_id=1)

        b2 = Bill(name="Thái Tấn Phát", email="ph345345attan@ou.edu.vn", amount_big=2, amount_young=3, phone="096548745",
                  address="81 Thống Nhất, P11, Gò Vấp, Thành Phố Hồ Chí Minh", cccd="214585214", pay_date="2023-01-12", total=939, product_id=7, user_id=2)

        b3 = Bill(name="Lê Văn Lâm", email="levanl345345am@ou.edu.vn", amount_big=4, amount_young=4, phone="0966287704",
                  address="89/23 Lê Thị Hồng, P3, Gò Vấp, Thành Phố Hồ Chí Minh", cccd="231415857", pay_date="2023-02-21", total=639, product_id=1, user_id=3)

        b4 = Bill(name="Nguyễn Thị Ngọc Yến", email="ngocy345345ennguyen@ou.edu.vn", amount_big=10, amount_young=6, phone="01662458451",
                  address="8929 Vườn Lài, P5, Quận 12, Thành Phố Hồ Chí Minh", cccd="236585214", pay_date="2023-02-21", total=6070, product_id=4, user_id=4)

        b5 = Bill(name="Nguyễn Thị Thanh", email="thanhje345435nny@ou.edu.vn", amount_big=3, amount_young=1, phone="0954781452",
                  address="1054 Quang Trung, P15, Gò Vấp, Thành Phố Hồ Chí Minh", cccd="202145281", pay_date="2023-01-08", total=358, product_id=3, user_id=5)

        b6 = Bill(name="Phan Thị Yến Vi", email="yenvi345345phan@ou.edu.vn", amount_big=10, amount_young=3, phone="0166875474",
                  address="84/21 Cách Mạng Tháng 8, P1, Quận 10, Thành Phố Hồ Chí Minh", cccd="254175845", pay_date="2023-01-01", total=1001, product_id=10, user_id=6)

        b7 = Bill(name="Nguyễn Toàn Mỹ", email="mynguy345345en@ou.edu.vn", amount_big=2, amount_young=4, phone="0165485741",
                  address="32/12 Nguyễn Thái Sơn, P3, Gò Vấp, Thành Phố Hồ Chí Minh", cccd="236598541", pay_date="2023-01-05", total=464, product_id=14, user_id=7)

        db.session.add_all([b1, b2, b3, b4, b5, b6, b7])
        db.session.commit()
