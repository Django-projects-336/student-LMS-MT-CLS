from django.contrib import admin
from .models import StudentDetail


# Register your models here.

class StudentAdmin(admin.ModelAdmin) :
        list_display = ("student_name", "email", "course", "enrollment_date")
        search_fields = ("student_name", "email", "course")
        list_filter = ("course",)  # ("course")
        
admin.site.register(StudentDetail, StudentAdmin)