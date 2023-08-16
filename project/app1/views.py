from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,"layout.html")

def AdminLogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pswd']
        try:
            newuser=AdminDataBase.objects.get(email=email)
            if newuser:
                if newuser.Password==password:
                    data=QueryDataBase.objects.all()
                    context={'data':data}
                    return render(request,"adminshowdata.html",context)
                else:
                    msg="Invalid User Email or Password"
                    return render(request,"AdminLogin.html",{'msg':msg})
        except:
            msg="Invalid User Email"
            return render(request,"AdminLogin.html",{'msg':msg})
    else:
        return render(request,"AdminLogin.html")



def AdminRegistration(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        Password=request.POST['pswd']
        cpswd=request.POST['cpswd']
        user=AdminDataBase.objects.filter(email=email)
        if user:
            msg="User alredy exist"
            return render(request,"AdminRegistration.html",{'msg':msg})
        else:
            if Password==cpswd:
                AdminDataBase.objects.create(name=name,email=email,contact=number,Password=Password)
                msg="User Register Successfully"
                return render(request,"AdminLogin.html",{'msg':msg})
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(request,"AdminRegistration.html",{'msg':msg})

    return render(request,"AdminRegistration.html")

def UserLogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pswd']
        try:
            newuser=UserDataBase.objects.get(uemail=email)
            if newuser:
                if newuser.uPassword==password:
                    return render(request,"Userpage.html")
                else:
                    msg="Invalid Email or Password"
                    return render(request,"UserLogin.html",{'msg':msg})
        except:
            msg="Invalid User Email"
            return render(request,"UserLogin.html",{'msg':msg})
    else:
        msg="user dose not exist"
        return render(request,"UserLogin.html")

def UserRegistration(request):
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            number=request.POST['number']
            Password=request.POST['pswd']
            cpswd=request.POST['cpswd']
            user=UserDataBase.objects.filter(uemail=email)
            if user:
                msg="User alredy exist"
                return render(request,"UserRegistration.html",{'msg':msg})
            else:
                if Password==cpswd:
                    UserDataBase.objects.create(uname=name,uemail=email,ucontact=number,uPassword=Password)
                    msg="User Register Successfully"
                    return render(request,"UserLogin.html",{'msg':msg})
                else:
                    msg = "Password and Confirm Password Doesnot Match"
                    return render(request,"UserRegistration.html",{'msg':msg})
        return render(request,"UserRegistration.html")


def Userpage(request):
    if request.method=="POST":
        nm=request.POST['qname']
        adrs=request.POST['qaddress']
        email=request.POST['qemail']
        phone=request.POST['qphone']
        query=request.POST['query']
        QueryDataBase.objects.create(qname=nm,qaddress=adrs,qemail=email,qphone=phone,query=query)
        return render(request,"Userpage.html")
    return render(request,"Userpage.html")

def showdata(request):
    data=QueryDataBase.objects.all()
    context={'data':data}
    return render(request,"showdata.html",context)

def Userdelete(request,id):
    data=QueryDataBase.objects.get(id=id)
    data.delete()
    return redirect('showdata')

def Userupdate(request,id):
    data=QueryDataBase.objects.get(id=id)
    if request.method=="POST":
        nm=request.POST['qname']
        adrs=request.POST['qaddress']
        email=request.POST['qemail']
        phone=request.POST['qphone']
        query=request.POST['query']
        data.qname=nm
        data.qaddress=adrs
        data.qemail=email
        data.qphone=phone
        data.query=query
        data.save()
        return redirect('showdata')
    return render(request,"Userupdate.html",{'data':data})






