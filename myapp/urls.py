from django.urls import path
from myapp.views import *

urlpatterns = [
    path('student-list', student_list, name='student-list'),
]
