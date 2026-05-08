from django.shortcuts import render
from .models import StudentDetail
from .forms import StudentForm



# Create your views here.
def homepage(request) :
        students_list = StudentDetail.objects.all()
        context  = {
                "students" : students_list
        }
        return render(request, "homepage.html" , context)

def add_student(request) :
        form = StudentForm()
        context = {
                "form" : form
        }
        return render(request, "add_student.html" , context)