from django.contrib import admin
from django.urls import path
from mediapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='index'),
    path('starter/', views.starter,name='starter-page'),
    path('about/', views.about ,name='about'),
    path('services/', views.services,name='services'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('appointment/', views.appointment,name='appointment'),
    path('contact/', views.contact,name='contact'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete,),
    path('displaycontacts/', views.displaycontacts, name='contacts'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    #MPESA API
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
