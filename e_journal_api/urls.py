from django.urls import path
from .views import *

urlpatterns = [
    path('student_api', StudentApiView.as_view()),
    path('group/<int:group_id>/', GroupDetailApiView.as_view()),
]
