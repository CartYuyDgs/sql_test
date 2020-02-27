from flask_script import Manager,Command,Option
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from apps.model import User,UserId,One,Book,Teacher,Classes

manage = Manager(app)
magrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)

'''
管理数据库版本命令，这几个命令暂时不要用，等数据库关联信息写好了之后再用
#初始化 DB Migrate
python manage.py db init
# 开始第跟踪
python manage.py db migrate -m "add leader"
# 根据记录文件生成数据库
python manage.py db upgrade
# 获取 History ID
python manage.py db history
# 回滚到某个 history
python manage.py db downgrade <history_id>

添加管理员命令
python manage.py addLeader -n yuy -t 18888888888 -e aaa@126.com -p 111111
'''

@manage.option('-n', '--user_name', dest='user_name')
@manage.option('-a', '--user_age', dest='user_age')
@manage.option('-i', '--user_id', dest='user_id')
def addUser(user_name, user_age, user_id):
    leader = User(user_name=user_name, user_age=user_age, user_id=user_id)
    db.session.add(leader)
    try:
        db.session.commit()
        print("user添加成功！")
    except Exception as e:
        print(e)
        db.session().rollback()
        return False
    return True

# class addUserid(Command):
#     option_list = (
#         Option('-card','-c',dest='card')
#     )
#
#     def run(self,card):
@manage.option('-c', '--card', dest='card')
def setuserid(card):
    userid = UserId(card=card)
    db.session.add(userid)
    db.session.commit()
    print('userid add success: '+card)

@manage.option('-n', '--one_name', dest='one_name')
@manage.option('-i', '--one_id', dest='one_id')
@manage.option('-a', '--one_age', dest='one_age')
@manage.option('-b1', '--one_book1', dest='one_book1')
@manage.option('-b2', '--one_book2', dest='one_book2')
def addOne(one_name,one_id,one_age,one_book1,one_book2):
    one = One(one_name=one_name,one_id=one_id,one_age=one_age)
    one.book = [Book(book_name=one_book1),Book(book_name=one_book2)]
    db.session.add(one)
    db.session.commit()
    print("添加ONE成功！")

#python manage.py addtc -t1 teacher1 -n1 t1111 -t2 teacher2 -n2 t2222 -c1 math -o1 c1111 -c2 chinese -o2 c2222
@manage.option('-t1', '--Teachername1', dest='Teachername1')
@manage.option('-n1', '--tno', dest='tno')
@manage.option('-t2', '--Teachername2', dest='Teachername2')
@manage.option('-n2', '--tno2', dest='tno2')
@manage.option('-c1', '--Classe1', dest='Classe1')
@manage.option('-o1', '--cno', dest='cno')
@manage.option('-c2', '--Classe2', dest='Classe2')
@manage.option('-o2', '--cno2', dest='cno2')
def addtc(Teachername1,tno,Teachername2,tno2,Classe1,cno,Classe2,cno2):
    teacher1 = Teacher(tno=tno, name=Teachername1, age=30)
    teacher2 = Teacher(tno=tno2, name=Teachername2, age=30)
    classes1 = Classes(cno=cno, name=Classe1)
    classes2 = Classes(cno=cno2, name=Classe2)
    teacher1.classes = [classes1, classes2]
    teacher2.classes = [classes1, classes2]
    classes1.teachers = [teacher1, teacher2]
    classes2.teachers = [teacher1, teacher2]
    db.session.add(teacher1)
    db.session.add(teacher2)
    db.session.add(classes1)
    db.session.add(classes2)
    db.session.commit()
    print("信息添加成功")


if __name__ == '__main__':
    manage.run()