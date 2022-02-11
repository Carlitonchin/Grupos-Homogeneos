from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'studentsInfo/index.html', {'students':students})
