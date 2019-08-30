from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import randint
from .util import *
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def IndexPage2(request):
    return render(request,"app/index2.html")

def registerUser(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    otp = randint(10000,99999)
    profilepic = request.FILES['image']
    newuser = User.objects.create(username=username,email=email,password=password,otp=otp,profilepic=profilepic)
    email_subject = "Doctor Finder : Account Vericication"
    sendmail(email_subject, 'mail_template', email, {
                             'name': username, 'otp': otp, 'link': 'http://localhost:8000/enterprise/user_verify/'})
    return HttpResponseRedirect(reverse('showdetail'))


def ShowDetail(request):
    all_user = User.objects.all()
    return render(request,"app/home.html",{'all_user':all_user})