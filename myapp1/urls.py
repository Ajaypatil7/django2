from myapp1 import views
from django.urls import path


urlpatterns = [
    path('home/', views.home, name='home'), 
    path('home_page/', views.home_page, name='home_page'),
    
]
