from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path
    method_req = request.method
    return HttpResponse(f"""
                        <p>Host: {host} </p>
                        <p>Path: {path} </p>
                        <p>User_agent: {user_agent} </p>
                        <p>requst method: {method_req} </p>                    
                        """)

def about(request, name, age):
    return HttpResponse(f"""<h2> О пользователе </h2>
                        <p>Имя: {name} </p>
                        <p>Возраст: {age}</p>""")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def user(request, name="Undefined", age = 0):
    return HttpResponse(f"""<h2>Имя: {name} </h2>
                        <h2> Возраст: {age} </h2>
                        """)