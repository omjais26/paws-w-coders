from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('food',views.food,name='food'),
    path('contact',views.contact,name='contact'),
    path('info',views.info,name='views')
]