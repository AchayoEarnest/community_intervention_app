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
    path('delete_ayp_enrollment_record/<int:enrollment_id>/', views.delete_ayp_enrollment_record, name="delete_ayp_enrollment_record" ),
    path('update_ayp_enrollment_record/<int:enrollment_id>/', views.update_ayp_enrollment_record, name="update_ayp_enrollment_record" ),
    path('api/', views.apiOverview, name="api-overview"),
    path('ayp-interventions/', views.ayp_interventions, name='ayp_interventions'),

    # api urls
    path('enrollment-list-api/', views.enrollmentList, name="enrollment-list-api"),
    path('enrollment-detail-api/<str:enrollment_id>', views.enrollmentDetail, name="enrollment-detail"),
    path('enrollment-create/', views.enrollmentCreate, name="enrollment-create"),
    path('enrollment-update/<str:enrollment_id>', views.enrollmentUpdate, name="enrollment-update"),
    path('enrollment-delete/<str:enrollment_id>', views.enrollmentDelete, name="enrollment-delete"),
]
