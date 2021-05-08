from django.urls import path
from . import views

urlpatterns = [
                path('', views.home, name='home'),
                path('login/', views.login , name='login'),
                path('submit/', views.submission_form, name='submission_form'),
                path('admin/',views.admin,name="Admin"),
                path('admin/user/<str:application_number>',views.viewMore,name="View More")
            ]