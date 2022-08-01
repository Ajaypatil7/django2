from myapp2 import views
from django.urls import path

urlpatterns = [
    path('profile/', views.profile, name='profile'), 
    path('profile_page/', views.profile_page, name='profile_page'), 
]
