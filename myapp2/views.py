from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return HttpResponse('<h2> Profile page is Displayed</h2>')
def profile_page(request):
    return render(request, 'profile_page.html')


