from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('cabinet/', cabinetView, name='cabinet'),
    path('student_cabinet/', studentCabinetView, name='student_cabinet'),
    path('students/', allStudentsList, name='all_students'),
    path('student_change_info/', changeStudentView, name='change_student'),
    path('add_new_subjects/', teacherAddSubjectsView, name='add_subjects'),
    path('', homeView, name='home'),
]
