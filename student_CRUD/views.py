from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse 
from .models import StudentDetail
from .forms import StudentForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer


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
        if request.method == "POST" :
                student = get_object_or_404(StudentDetail, pk=id)
                form = StudentForm(request.POST, instance=student)
                if form.is_valid() :
                        form.save()
                        return redirect("homepage")
        
        student = get_object_or_404(StudentDetail,pk=id)
        form = StudentForm(instance=student)
        context = {
              "form" : form
      }
        return render(request, "view_details.html", context)

def delete_student(request, id) :
        student = get_object_or_404(StudentDetail, pk=id)
        student.delete()
        return redirect("homepage")

#  API Creation
class StudentListCreateAPI(APIView) :
        def get(self , request) :
                students = StudentDetail.objects.all()
                serializer = StudentSerializer(students , many= True)
                return Response(serializer.data , 
                                status=status.HTTP_200_OK)