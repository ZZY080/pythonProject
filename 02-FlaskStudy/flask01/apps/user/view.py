import hashlib

from flask import  Blueprint,render_template,request,redirect,url_for
from sqlalchemy import or_

from apps.user.models import User
from exts import db

user_bp=Blueprint('user',__name__)
# @user_bp.route('/register',methods=['POST','GET'])
# def register():
#     if request.method=='POST':
#         username=request.form.get('username')
#         password=request.form.get('password')
#         repassword=request.form.get('repassword')
#         phone=request.form.get('phone')
#         if password==repassword:
#             user=User()
#             user.username=username
#             user.password=hashlib.sha256(password.encode('utf-8')).hexdigest()
#             user.phone=phone
#
#             db.session.add(user)
#             db.session.commit()
#             return  redirect(url_for('user.user_center'))
#
#
#     return  render_template('/user/register.html')
#
# @user_bp.route('/')
# def user_center():
#     users=User.query.filter(User.isdelete==False).all()
#     print(users)
#     return render_template('user/center.html',users=users)
#
# @user_bp.route('/login',methods=['POST','GET'])
# def login():
#     if request.method=='POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         new_password=hashlib.sha256(password.encode('utf-8')).hexdigest()
#         user_list=User.query.filter_by(username=username)
#         for u in user_list:
#             if u.password==new_password:
#                 return '用户登录成功！'
#         else:
#             return render_template('user/login.html',msg='用户名或密码有误')
#         return 'testing'
#
#     return render_template('user/login.html')
#
#
# @user_bp.route('/search')
# def search():
#     keyword=request.args.get('search')
#
#     user_list=User.query.filter(or_(User.username.contains(keyword),User.phone.contains(keyword))).all()
#     return render_template('user/center.html',users=user_list)
#
# @user_bp.route('/delete',endpoint='delete')
# def user_delete():
#     id=request.args.get('id')
#     user=User.query.get(id)
#     user.isdelete=True
#     db.session.commit()
#     return  redirect(url_for('user.user_center'))
#
# @user_bp.route('/update',endpoint='update',methods=['GET','POST'])
# def user_update():
#     if request.method=='POST':
#         username=request.form.get('username')
#         phone=request.form.get('phone')
#         id=request.form.get('id')
#         user=User.query.get(id)
#         user.phone=phone
#         user.username=username
#         db.session.commit()
#         return redirect(url_for('user.user_center'))
#     else:
#         id=request.args.get('id')
#         user=User.query.get(id)
#
#         return  render_template('user/update.html',user=user)
