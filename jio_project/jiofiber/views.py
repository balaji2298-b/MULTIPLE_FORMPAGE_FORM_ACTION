from django.shortcuts import render, redirect
from .models import Student
from .models import Staff
from .models import Parents

def index(request):
    return render(request, "index.html")

def staff(request):
    return render(request, "staffreg.html")

def parents(request):
    return render(request, "parentsreg.html")

def student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        fees = request.POST.get("fees")
        student = Student(name=name, course=course, fees=fees)
        student.save()
        return redirect("index")

    return render(request, "studentreg.html")

def parents(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        parents = Parents(name=name, contact=contact,)
        parents.save()
        return redirect("index")

    return render(request, "parentsreg.html")

def staff(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        experience = request.POST.get("experience")
        dept = request.POST.get("dept")
        staff = Staff(name=name, contact=contact, experience=experience, dept=dept)
        staff.save()
        return redirect("index")
    else:
        return render(request, "staffreg.html")


