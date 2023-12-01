from django.urls import  path,include
from book.views import bookList,index,detail,set_cookie,get_cookie,get_seeeion,set_session,login,LoginView,middleware,home
urlpatterns=[
    path('booklist/index', index),
    path('booklist',bookList,name='book1'),
    path('detail/<int:category_id>/<int:book_id>/', detail),
    path('setcookie/',set_cookie),
    path('getcookie/',get_cookie),
    path('setsession/',set_session),
    path('getsession/',get_seeeion),
    path('login', login),
    path('login2', LoginView.as_view()),
    path('middleware',middleware),
    path('home', home)

]