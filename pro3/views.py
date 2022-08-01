from django.http import HttpResponse
from django.shortcuts import render

def login(request,a):
    return HttpResponse(f'<h1>Login Is {a} displayed</h1>')

def login_page(request,n):
    print(n)
    return render(request, 'login.html', context={"n":n})

def html_demo(request,name):
    login=True
    return render(request, 'html_demo.html', context={'login':login, 'name':'Ajay'})
