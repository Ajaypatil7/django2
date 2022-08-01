from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h2>Home PAge is Displayed<h2>')
def home_page(request):
    return render(request , 'home_page.html')