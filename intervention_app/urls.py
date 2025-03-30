from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('reports/', views.reports, name='reports'),
    path('enrollment_list/', views.add_enrollment, name="enrollment_list"),
    path('enrollments/add/', views.add_enrollment, name="add_enrollment"),
    path('interventions/add/<int:enrollment_id>/', views.add_intervention, name="add_intervention"),
    path('ayp_enrollment_record/<int:enrollment_id>/', views.ayp_enrollment_record, name="ayp_enrollment_record"),
    path('delete_ayp_enrollment_record/<int:enrollment_id>/', views.delete_ayp_enrollment_record, name="delete_ayp_enrollment_record" )

]
