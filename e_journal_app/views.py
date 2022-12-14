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
