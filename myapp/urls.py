from myapp import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('event/', views.Eventgenerics.as_view()),
    path('user/', views.Usergenerics.as_view())
    
]
