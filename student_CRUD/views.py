from django.shortcuts import render

# Create your views here.
def homepage(request) :
        return render(request, "homepage.html")

def add_student(request) :
        return render(request, "add_student.html")