from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('student_cabinet/', studentCabinetView, name='student_cabinet'),
    path('', homeView, name='home'),
]
