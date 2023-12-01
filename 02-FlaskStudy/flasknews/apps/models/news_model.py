from exts import  db
from apps.models import  BaseModel
class NewsType(BaseModel):
    __tablename__='news_type'
    type_name=db.Column(db.String(50),nullable=False)
    newsList=db.relationship('News',backref='newstype')

class News(BaseModel):
    __tablename__='news'
    title=db.Column(db.String(100),nullable=False)
    desc=db.Column(db.String(255),nullable=False)
    content=db.Column(db.TEXT,nullable=False)
    news_type_id=db.Column(db.Integer,db.ForeignKey('news_type.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

class  Comment(BaseModel):
    __tablename__='comment'
    content=db.Column(db.String(255),nullable=False)
    love_num=db.Column(db.Integer,default=0)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    news_id=db.Column(db.Integer,db.ForeignKey('news.id'))
    replys=db.relationship('Reply',backref='comment')

class Reply(BaseModel):
    __tablename__='reply'
    content=db.Column(db.String(255),nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id=db.Column(db.Integer,db.ForeignKey('comment.id'))


