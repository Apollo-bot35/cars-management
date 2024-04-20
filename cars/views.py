from django.shortcuts import render,redirect
from django.contrib import messages
from .services import Carservices



def home(request):
    return render(request,'index.html')

def registerc(request):
    return render(request,'admin1.html')

def customers(request):
    return render(request,'registration.html')

def car(request):
     return render(request,'carregister.html')

def caradd(request):
     mess=None
     if request.method=="POST":
          id=int(request.POST.get("carid"))
          mn=request.POST.get("modelnm")
          co=request.POST.get("company")
          pr=int(request.POST.get("price"))
          obj=Carservices()
          stat=obj.addca(id,mn,co,pr)
          if stat=="success":
               page="success.html"
          else:
            page="failed.html"

          
     

def login1(request):
    mess=None
    id=request.POST.get("username")
    pw=request.POST.get("password")
    obj=Carservices()
    stat=obj.login2(id,pw)
    if stat=="success":
            page="success.html"
    else:
            page="failed.html"
    return render(request,'dash.html')


def addcustomers(request):
    mess=None
    if request.method=="POST":
        id=int(request.POST.get("custid"))
        nm=request.POST.get("custname")
        ar=request.POST.get("address")
        no=int(request.POST.get("phoneno"))

        obj=Carservices()
        stat=obj.addcust(id,nm,ar,no)
        if stat=="success":
            page="success.html"
        else:
            page="failed.html"


    return render(request,page)

def showlist(request):
    obj=Carservices()
    data=obj.getalldata()
    return render(request,'Report.html',{"carlist":data})



