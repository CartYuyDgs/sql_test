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
    one_id = db.Column(db.Integer,db.ForeignKey('user_id.id'))
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

