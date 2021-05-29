from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
                path('', views.home, name='home'),
                path('admin/', views.adminLogin, name="login"),
                path('admin/profile/', views.admin, name="admin"),
                path('accounts/profile/', views.profile, name="profile"),
                # path('accounts/logout/', views.logout, name="logout"),
                path('submit/', views.submission_form, name='submission_form'),
                path('admin/user/<str:application_number>',views.viewMore,name="View More")
            ]