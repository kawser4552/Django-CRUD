from django.urls import path
from .views import *

app_name = 'crudapp'

urlpatterns = [
    
    path("",index,name ='index'),
    path("studentform/",studentform,name ='studentform'),
    path('student_info/<int:student_id>/',student_info,name="student_info"),
    path('student_update/<int:student_id>/',student_update,name="student_update"),
    path('student_delete/<int:student_id>',student_delete,name='student_delete'),
]