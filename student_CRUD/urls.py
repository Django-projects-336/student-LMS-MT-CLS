from django.contrib import admin
from django.urls import path 
from student_CRUD import views



urlpatterns = [
    path("", views.homepage, name="homepage"), 
    path("add-student/", views.add_student, name="add-student"), 
    path("details/<int:id>/", views.details, name="details")
]