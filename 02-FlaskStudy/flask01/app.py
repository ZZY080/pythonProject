from flask_script import Manager
from flask_migrate import  Migrate,MigrateCommand
from apps.user.models import  User
from apps.article.models import Article
from apps.article.models import *
from apps import  create_app
from exts import db

app=create_app()
#  以命令行的方式打开 app.py
manager=Manager(app=app)

migrate=Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)
if __name__=='__main__':
    manager.run()