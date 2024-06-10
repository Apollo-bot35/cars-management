from django.shortcuts import render,redirect
from django.contrib import messages
from .services import Carservices
import pymysql



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
               page="failed.html"
          else:
            page="success.html"
            return render(request,page)         
          
     

def login1(request):
   mess=None
   if request.method == 'POST':
        username = request.POST.get('usern')
        password = request.POST.get('password')
        
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from admin where userid='%s' and pswd='%s'" %(username,password))
        data=curs.fetchone()
        if data:
            page="dash.html"
        else:
            page="failed.html"
        con.close()

        return render(request,page)


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


def listcu(request):
    obj=Carservices()
    data=obj.getdata()
    return render(request,'blank.html',{"customerlist":data})

def searchca(request):
    return render(request,'searchcar.html')

def carsearch(request):
    if request.method=="POST":
        nm=request.POST.get("modelnm")
        obj=Carservices()
        data=obj.searchresult(nm)
    return render(request,'searchresult.html',data)

def searchcust(request):
    return render(request,'searchcust.html')

def custsearch(request):
    if request.method=="POST":
        ne=request.POST.get("custname")
        obj=Carservices()
        data=obj.searchresults(ne)
    return render(request,'searchresults.html',data)

def changes(request):
     return render(request,'changeprice.html')

def prichange(request):
    if request.method=="POST":
        nm=request.POST.get("modelnm")
        pri=float(request.POST.get("price"))
        obj=Carservices()
        stat=obj.changecarpri(nm,pri)
        return render(request,"pricechanged.html",{'status':stat})


def changeph(request):
    return render(request,'custdetails.html')

def phonechg(request):
    if request.method=="POST":
        nm=request.POST.get("custname")
        no=int(request.POST.get("phoneno"))
        obj=Carservices()
        stat=obj.changephn(nm,no)
        return render(request,"phonechange.html",{'status':stat})








