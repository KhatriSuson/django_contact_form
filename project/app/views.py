from django.shortcuts import render

# from .models import Contact, Student_detail, About_Me
from app.models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        # return HttpResponse("<h1> THANKS FOR CONTACT </h1>")
        return render(request, "hello.html")

    return render(request, "index.html")


def student_form(request):
    if request.method == "POST":
        std_detail = Student_detail()
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        zip = request.POST.get("zip")
        city = request.POST.get("city")
        state = request.POST.get("state")

        std_detail.name = name
        std_detail.email = email
        std_detail.address = address
        std_detail.zip = zip
        std_detail.city = city
        std_detail.state = state

        std_detail.save()
        # return render(request, "hello.html")

    return render(request, "student_form.html")


def about(requst):
    about0 = About_Me()

    about0.title = "title title of the page"
    about0.dis = "description of the page "

    about1 = About_Me()
    about1.title = "title one"
    about1.dis = "description of the page one "

    about2 = About_Me()
    about2.title = "title tw0"
    about2.dis = "description of the page tw0 "
    

    about = [about0, about1, about2]

    return render(requst, "about.html", {"about": about})


def stu_manage(request):
    
    stu1 = Stu_manage()
    stu1.title = "Product Title"
    stu1.product_dis = "product description one"

    stu2 = Stu_manage()
    stu2.title = "Product Title"
    stu2.product_dis = "product description two  Verify that your app_stu_manage model is correctly defined in your Django app. Ensure that you have the correct app name in your "

    stu = [stu1, stu2]

    return render(request, "stu_manage.html", {"stu": stu})


def Serives(request):

    return render(request,"service.html" )

def account(request):
    
    return render(request, 'accounts.html')