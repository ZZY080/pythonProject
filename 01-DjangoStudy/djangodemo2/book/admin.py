from django.contrib import admin
from book.models import PeopleInfo,BookInfo
# Register your models here.
admin.site.site_header='书籍管理'
admin.site.site_title='书籍管理'
admin.site.index_header='书籍管理'


admin.site.register(PeopleInfo)
admin.site.register(BookInfo)
