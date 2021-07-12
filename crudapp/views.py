from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    student = Student.objects.order_by("first_name")
    diction={'title':"index",'student':student}
    return render(request,"FirstApp/index.html",context=diction)

def studentform(request):
    form = StudentForm

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")

    diction={'title':"studentform",'student':form}
    return render(request,"FirstApp/studentform.html",context=diction)

def student_info(request,student_id):
    student_info = Student.objects.get(pk = student_id)
    dict = {'student':student_info}
    return render(request,"FirstApp/studentinfo.html",context=dict)

def student_update(request,student_id):
    student_info = Student.objects.get(id=student_id)
    form = StudentForm(instance=student_info)
    if request.method =="POST":
        form = StudentForm(request.POST,instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        

    diction = {'student':form}
    return render(request,"FirstApp/update.html",context=diction)

def student_delete(request,student_id):
    student = Student.objects.get(pk=student_id).delete()
    diction = {'msg':'delete done !'}
    return index(request)
    return render(request,"FirstApp/delete.html",context=diction)
