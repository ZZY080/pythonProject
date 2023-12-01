import datetime
import json

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.serializers import  serialize
from django.urls import  reverse
from django.views import View

from book.models import BookInfo,PeopleInfo
# Create your views here.

def middleware(request):
    print('view 视图被调用')
    return  HttpResponse('ok')

def detail(request,category_id,book_id):
    # print(category_id,book_id)
    # username=request.GET.get('username')
    # password=request.GET.get('password')
    # print(username,password)
    # usernames=request.GET.getlist('username')
    # print(usernames)
    # username=request.POST.getlist('username')
    # print(username)
    body_str=request.body.decode()
    print(body_str)
    data=json.loads(body_str)
    print(data)
    return  HttpResponse('detail')

def index(request):
    # return  redirect(reverse('book:book1'))
    return  HttpResponse('index')


def bookList(request):
    books=BookInfo.objects.all()
    d=serialize('json',books)
    return HttpResponse(d)


def set_cookie(request):
    username=request.GET.get('username')
    response=HttpResponse('set_cookie')
    response.set_cookie('username',username)
    return response
def get_cookie(request):
    cookies=request.COOKIES
    username=cookies.get('username')
    return  HttpResponse('get_cookie')

def set_session(request):
    print(request.COOKIES)
    user_id=666
    request.session['user_id']=user_id
    return  HttpResponse('set_session')
def get_seeeion(request):
    print(request.COOKIES)
    user_id=request.session['user_id']
    print(user_id)
    return  HttpResponse('get_session')

def login(request):
    print(request.method)
    if request.method=='PUT':
        return  HttpResponse('put')
    if request.method=='POST':
        return  HttpResponse('post')
    if request.method=='GET':
        return  HttpResponse('GET')
class LoginView(View):
    def get(self,request):
        return  HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')

    def patch(self, request):
        return HttpResponse('patch')

    def delete(self, request):
        return HttpResponse('delete')
def home(request):
    # 定义上下文
    context={
        "city":"北京",
        "username":"吴彦祖",
        "birthday":datetime.datetime.now(),
        "friends":["刘毓琇","崔玥","曾志远"],
        "money":{
            "2020":1200,
            "2010":130000,
            "2021":123456
        },
        "age":19,
        "desc":"<script>confirm('你好')</script>"

    }
    return render(request,"home.html",context)

