from exts import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from sqlalchemy.orm import relationship

#外键
class User(db.Model):
    __tablename__ = 'user_table'
    user_index = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(30))
    user_id = db.Column(db.Integer,db.ForeignKey('user_id.id'))
    user_age = db.Column(db.Integer,nullable=True)

class UserId(db.Model):
    __tablename__ = 'user_id'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    card = db.Column(db.String(20),nullable=True)

#一对多
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    book_name = db.Column(db.String(30))
    one_id = db.Column(db.Integer,db.ForeignKey('one_table.one_index'))
    book_one = relationship('One',back_populates='book')

class One(db.Model):
    __tablename__ = 'one_table'
    one_index = db.Column(db.Integer,primary_key=True,autoincrement=True)
    one_name = db.Column(db.String(30))
    # one_id = db.Column(db.Integer,db.ForeignKey('user_id.id'))
    one_age = db.Column(db.Integer,nullable=True)
    book = relationship('Book',order_by=Book.id,back_populates='book_one')

#多对多
association_table = db.Table('teacher_classes',
        db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')),
        db.Column('classes_id',db.Integer,db.ForeignKey('classes.id'))
                             )

class Teacher(db.Model):
    __tablename__='teacher'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    tno = db.Column(db.String(20))
    age = db.Column(db.Integer)
    classes = relationship('Classes',secondary=association_table,back_populates='teachers')

class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    cno = db.Column(db.String(20))
    teachers = relationship('Teacher',secondary=association_table,back_populates='classes')

class City(db.Model):
    __tablename__ = "apf_city"
    city_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(9),nullable=True)
    weather_id = db.Column(db.String(11),nullable=True)
    name = db.Column(db.String(16),nullable=True)
    status = db.Column(db.String(1),nullable=True, default = '0')
    province_id = db.Column(db.Integer, db.ForeignKey("apf_province.province_id"))
    province = relationship("Province", back_populates='city')

class Province(db.Model):
    __tablename__ = "apf_province"
    province_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),nullable=True)
    city = relationship("City",back_populates='province')

class User01(db.Model):
    __tablename__ = 'user01'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    article01 = relationship("Article01",back_populates='auther')

    __mapper_args__ = {
        "order_by": username
    }

    def __repr__(self):
        return "<User01 username:%s>"%self.username

class Article01(db.Model):
    __tablename__ = "article01"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30),nullable=True)
    context = db.Column(db.Text)

    uid = db.Column(db.Integer, db.ForeignKey("user01.id"))
    auther = relationship("User01", back_populates="article01")

    __mapper_args__ = {
        "order_by": title
    }

    def __repr__(self):
        return "<User01 title:%s,uidL%d >"%(self.title,self.uid)


