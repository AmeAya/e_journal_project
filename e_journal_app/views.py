from django.shortcuts import render
from .models import *

# Create your views here.
def homeView(request):
    thisUser = request.user
    subjects = Subject.objects.all() # get all data from table Subject
    try:
        thisStudent = Student.objects.get(user_id=thisUser) # get data from table Student
        thisUserType = 'Student'
    except:
        thisUserType = 'Teacher'
    return render(request,
                  template_name='home.html',
                  context={
                      'type': thisUserType,
                      'subjects': subjects
                  }) # context - datas to show on template

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
