from rest_framework import serializers
from .models import StudentDetail

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model = StudentDetail
                fields = ["id","student_name" , "email" , "course" , "enrollment_date"]