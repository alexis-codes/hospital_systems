from django.contrib import admin
from django.urls import path
from mediapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('starter/', views.starter,name='starter-page'),
    path('about/', views.about ,name='about'),
    path('services/', views.services,name='services'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('appintment/', views.appointment,name='appointment'),

]
