from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse 
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
        if request.method == "POST" :
                form = StudentForm(request.POST)
                if form.is_valid() :
                        form.save()
                        return redirect("homepage")
        
        form = StudentForm()
        context = {
                "form" : form
        }
        return render(request, "add_student.html", context)

def details(request, id) :
      student = get_object_or_404(StudentDetail,pk=id)
      form = StudentForm(instance=student)
      context = {
              "form" : form
      }
      return render(request, "view_details.html", context)