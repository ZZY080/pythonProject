import datetime

from exts import  db

class Friend(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    uid=db.Column(db.Integer,db.ForeignKey('user.id'))
    fid=db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(15),nullable=False)
    password=db.Column(db.String(12),nullable=False)
    udatetime=db.Column(db.DateTime,default=datetime.datetime.now)
    phone=db.Column(db.String(11))
    icon=db.Column(db.String(150))
    email=db.Column(db.String(100))
    isdelete=db.Column(db.Boolean)
    friends=db.relationship('Friend',backref='user',foreign_keys=Friend.uid)

