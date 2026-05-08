from django import forms
from .models import StudentDetail


class StudentForm(forms.ModelForm) :
        class Meta :
                model = StudentDetail
                fields = ["student_name", "email", "course", "enrollment_date"]
                