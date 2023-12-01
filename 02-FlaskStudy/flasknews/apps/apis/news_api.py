from flask import  Blueprint
from flask_restful import Api, Resource, fields, marshal_with, reqparse, marshal
from apps.models.news_model import NewsType, News
from exts import db

news_bp=Blueprint('news',__name__)
api=Api(news_bp)
types_fields={
    'id':fields.Integer,
    'name':fields.String(attribute='type_name')

}
# 传入
type_parser=reqparse.RequestParser()
type_parser.add_argument('typeName',type=str,required=True,help='必须添加新闻分类名字',location='form')
# 修改传入
update_type_parser=type_parser.copy()
update_type_parser.add_argument('id',type=int,required=True,help='必须添加要修改的分类id')
# 删除的传入
delete_type_parser=reqparse.RequestParser()
delete_type_parser.add_argument('id',type=int,required=True,help='必须添加要修改的分类id')
class NewsTypeApi(Resource):
    @marshal_with(types_fields)
    def get(self):
        types=NewsType.query.all()
        return  types

    # 使用post添加新闻类型
    def post(self):
        args=type_parser.parse_args()
        typeName=args.get('typeName')
        # 数据库添加
        newsType=NewsType()
        newsType.type_name=typeName
        db.session.add(newsType)
        db.session.commit()
        return  marshal(newsType,types_fields)
    # 修改分类名称
    def patch(self):
        # 获取传入的值
        args=update_type_parser.parse_args()
        # 获取id
        typeId=args.get('id')
        new_type_name=args.get('typeName')
        # 修改
        type_obj=NewsType.query.get(typeId)
        if type_obj:
            type_obj.type_name=new_type_name
            db.session.commit()
            data={
                'status':200,
                'msg':'修改成功',
                'type':marshal(type_obj,types_fields)
            }
            return  data
        else:
            data={
                'status':400,
                'msg':'类型查找失败！'
            }
            return data

    # 删除分类名称
    def delete(self):
        args=delete_type_parser.args()
        typeId=args.get('id')
        type_obj=NewsType.query.get(typeId)
        if type_obj:
            db.session.delete(type_obj)
            db.session.commit()
            data={
                'status':200,
                'msg':'类型删除成功',
            }
        else:
            data={
                'status':400,
                'msg':'类型查找失败'
            }
        return data



# 传入
news_parser=reqparse.RequestParser()
news_parser.add_argument('typeid',type=int,help='必须添加新闻类型id',required=True)
news_parser.add_argument('page',type=int)
# 输出
class AuthorName(fields.Raw):
    def format(self, value):
        return value.username
# 每条新闻的格式
naews_fields={
    'id':fields.Integer,
    'title':fields.String,
    'desc':fields.String,
    'datetime':fields.DateTime(attribute='date_time'),
    'author':AuthorName(attribute='author'),
    'url':fields.Url('newsdetail',absolute=True)
}
# 新闻api
class NewsListApi(Resource):
    # 获取某个新闻分类下的新闻
    def get(self):
        args=news_parser.parse_args()
        typeid=args.get('typeid')
        page=args.get('page',1)
        pagination=News.query.filter(News.news_type_id==typeid).paginate(page=page,per_page=8)
        data={
            'has_more':pagination.has_next,
            'data':pagination.items,
            'return_count':len(pagination.items),
            'html':'null',
        }
        return  data

# 回复格式
reply_fields={
    'user':AuthorName(attribute='user'),
    'content':fields.String,
    'datetime':fields.DateTime(attribute='date_time'),
    'lovenumber':fields.Integer(attribute='love_num')
}

# 评论的格式
comment_fields={
    'user':AuthorName(attribute='user'),
    'content':fields.String,
    'datetime':fields.DateTime(attribute='date_time'),
    'lovenumber':fields.Integer(attribute='love_num'),
    'replys':fields.List(fields.Nested(reply_fields))
}
news_detail_fields={
    'id':fields.Integer,
    'title':fields.String,
    'content':fields.String,
    'data-time':fields.DateTime(attribute='date_time'),
    'author':AuthorName(attribute='author'),
    'comments':fields.List(fields.Nested(comment_fields))
}
class NewsDetailApi(Resource):
    @marshal_with(news_detail_fields)
    def get(self,id):
        news=News.query.get(id)
        return  news

    # def post(self):
    #     pass

class NewsApi(Resource):
    def post(self):
        pass
    def patch(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass




api.add_resource(NewsTypeApi,'/types')
api.add_resource(NewsListApi,'/newslist')
api.add_resource(NewsDetailApi,'/newsdetail/<int:id>',endpoint='newsdetail')