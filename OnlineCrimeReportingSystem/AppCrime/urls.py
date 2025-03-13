from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('Admin_login/', views.Admin_login, name='Admin_login'),
    path('User_login/', views.User_login, name='User_login'),
    path('Register/', views.Register, name='Register'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
    path('ViewUser/', views.ViewUser, name='ViewUser'),
    
    path('Complain/', views.Complain, name='Complain'),
    path('ComplaintStatus/', views.ComplaintStatus, name='ComplaintStatus'),
    path('MissingPersons/', views.MissingPersons, name='MissingPersons'),
    path('ViewComplaints/', views.ViewComplaints, name='ViewComplaints'),
    path('CheckReport/', views.CheckReport, name='CheckReport'),
    path('UpdateComplaint/', views.UpdateComplaint, name='UpdateComplaint'),
    path('UpdateMissingComplaint/', views.UpdateMissingComplaint, name='UpdateMissingComplaint'),
       
]



