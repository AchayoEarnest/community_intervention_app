from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('reports/', views.reports, name='reports')
    path('enrollments/add/', add_enrollment, name="add-enrollment")
]
