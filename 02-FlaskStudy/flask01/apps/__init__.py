from flask import  Flask
import settings
from apps.article.views import article_bp1
from apps.user.views import user_bp1
from exts import db, bootstrap, cache

config={
    'CACHE_TYPE':'redis',
    'CACHE_REDIS_HOST':'127.0.0.1',
    'CACHE_REDIS_PORT':6379

}

def create_app():
    app=Flask(__name__,template_folder='../templates',static_folder='../static')
    #  配置
    app.config.from_object(settings.DevelopmentConfig)
    # 初始化db
    db.init_app(app=app)
    bootstrap.init_app(app=app)
    cache.init_app(app=app,config=config)
    # 注册蓝图
    # app.register_blueprint(user_bp)
    app.register_blueprint(user_bp1)
    app.register_blueprint(article_bp1)
    return app