from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def homeView(request):
    thisUser = request.user
    try:
        thisStudent = Student.objects.get(user_id=thisUser) # get data from table Student
        thisUserType = 'Student'
        subjects = Subject.objects.all()
        return render(request,
                      template_name='home.html',
                      context={
                          'type': thisUserType,
                          'subjects': subjects
                      })
    except:
        thisUserType = 'Teacher'
        thisTeacher = Teacher.objects.get(user_id=request.user.id)
        subjects = thisTeacher.subject
        return render(request,
                      template_name='home.html',
                      context={
                          'type': thisUserType,
                          'subjects': subjects
                      })

def cabinetView(request):
    try:
        Student.objects.get(user_id=request.user)
        return redirect('student_cabinet')
    except:
        return redirect('home')

def studentCabinetView(request):
    thisStudent = Student.objects.get(user_id=request.user)
    thisGroup = thisStudent.group
    thisGrades = Grade.objects.filter(student=thisStudent)
    # filter - get many records from table with (student=thisStudent) condition
    return render(request,
                  'student_cabinet.html',
                  context={
                      'student': thisStudent,
                      'group': thisGroup,
                      'grades': thisGrades
                  })

def allStudentsList(request):
    students = Student.objects.all()
    return render(request,
                  'students.html',
                  context={
                      'students': students
                  })
