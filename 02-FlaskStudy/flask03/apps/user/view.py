import os

from flask import Blueprint, url_for
from flask_restful import Resource, fields, marshal_with, reqparse, inputs, marshal
from werkzeug.datastructures import FileStorage

from apps.user.model import User, Friend
from exts import api, db
from settings import Config

user_bp=Blueprint('user',__name__,url_prefix='/api')

class IsDelete(fields.Raw):
    def format(self, value):
        print('--------',value)
        return  'Normal'
user_fields_1={
    'id':fields.Integer,
    'username':fields.String(default='匿名'),
    'uri':fields.Url('single_user',absolute=True)

}
user_fields={
    'id':fields.Integer,
    'username':fields.String(attribute='username',default='匿名'),
    'pwd':fields.String(attribute='password'),
    'isDelete':fields.String(attribute='isdelete'),
    'isDelete1':IsDelete(attribute='isdelete'),
    'udatetime':fields.DateTime(dt_format='rfc822'),
}

# 参数解析
parser=reqparse.RequestParser(bundle_errors=True)  # 解析对象 request.form.get() request.args.get()  request.cookies.get()  request.headers.get()
parser.add_argument('username',type=str,required=True,help='必须输入用户名',location=['form'])
parser.add_argument('password',type=inputs.regex(r'^\d{6,12}$'),required=True,help='必须输入6-12位数字密码',location=['form'])
parser.add_argument('phone',type=inputs.regex(r'^1[356789]\d{9}$'),location=['form'],help='手机号码格式错误')
parser.add_argument('hobby',action='append')
parser.add_argument('icon',type=FileStorage,location=['files'])
# 定义类的视图
class UserResource(Resource):
    # get 请求处理
    @marshal_with(user_fields_1)
    def get(self):
        users=User.query.all()
        return users


    # post
    @marshal_with(user_fields)
    def post(self):
        args=parser.parse_args()
        username=args.get('username')
        password=args.get('password')
        phone=args.get('phone')
        bobby=args.get('hobby')
        icon=args.get('icon')

        # 创建user对象
        user=User()
        user.username=username
        user.password=password
        if icon:
            upload_path = os.path.join(Config.UPLOAD_ICON_DIR, icon.filename)
            icon.save(upload_path)
            # 保存这个路径
            user.icon = os.path.join('upload/icon', icon.filename)
        if phone:
            user.phone = phone
        db.session.add(user)
        db.session.commit()

        return user

    # put
    def put(self):
        print('endoint的使用',url_for('all_user'))
        return {'msg':'---------put'}
    # delete
    def delete(self):
        return {'msg':'-------delete'}

class UserSimpleResource(Resource):
    @marshal_with(user_fields_1) # user转成一个序列化对象
    def get(self,id):
        user=User.query.get(id)
        return user  # 不是 str list int
    def put(self,id):
        print('endpoint的使用:',url_for('all_user'))
        return {'msg':'ok'}
    def delete(self,id):
        pass

user_friend_fields={
    'username': fields.String,
    'nums': fields.Integer,
    'friends': fields.List(fields.Nested(user_fields))
}
class UserFriendResource(Resource):
    @marshal_with(user_friend_fields)
    def get(self,id):

        friends=Friend.query.filter(Friend.uid==id).all()
        user=User.query.get(id)
        print(user)
        print(friends,user)
        friend_list=[]
        for friend in friends:
            u=User.query.get(friend.fid)
            friend_list.append(u)
        # data={
        #     'username':user.username,
        #     'nums':len(friends),
        #     'friends':marshal(friend_list,user_fields)
        # }
        data={
            'username':user.username,
            'nums':len(friends),
            'friends':friend_list,
        }
        return  data

api.add_resource(UserResource,'/user',endpoint='all_user')
api.add_resource(UserSimpleResource,'/user/<int:id>',endpoint='single_user')
api.add_resource(UserFriendResource,'/friend/<int:id>',endpoint='user_friend')
