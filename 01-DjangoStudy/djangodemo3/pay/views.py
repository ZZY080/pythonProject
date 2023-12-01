from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import threading

count =0

def handle_request(request,count):
    print(count)
    return HttpResponse(f"{count}")

def index(request):
    global count
    count+=1
    for i in range(100):
        thread = threading.Thread(target=handle_request, args=(request, count))
        thread.start()
    return  HttpResponse(f"{count}");
