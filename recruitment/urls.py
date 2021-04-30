from django.urls import path
from . import views

urlpatterns = [
                path('', views.login, name='login'),
                path('home/', views.home, name='home'),
                path('submit/', views.submission_form, name='submission_form'),
                path('submit/admin/',views.admin,name="Admin"),
            ]
