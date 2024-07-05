from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.
def studentslist(request):

    get_students = Student.objects.all()
    data = {
        'get_students' : get_students,
    }
    return render(request, 'studentlist.html', data)

