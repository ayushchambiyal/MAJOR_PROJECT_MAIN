from multiprocessing import context
from subprocess import check_output
from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from home.models import Signup
from home.models import Item,cont_me
from django.shortcuts import redirect
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):

    return render(request,'index.html')
    #return HttpResponse('This Is Home Page')

def about(request):
    return render(request,'about.html')

def seller(request):
    return render(request,'seller.html')

def buyer(request):
    return render(request,'buyer.html')

def contact(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        message=request.POST.get('message')
        cont=cont_me(first_name=first_name,last_name=last_name,email=email,gender=gender,message=message)
        cont.save()
        messages.success(request,"We Will Revert You Shortly")
        
    return render(request,'contact.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1') 
        password2=request.POST.get('password2')
        signup=Signup(first_name=first_name,last_name=last_name,email=email,password1=password1,password2=password2)
        signup.save()

        messages.success(request,"::))")
    return render(request,'register.html')

#@login_required(login_url='login')
def seller_interface(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.seller_name=request.POST.get('seller_name')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
        
        prod.dtime=request.POST.get('datetime')

        prod.save()
        messages.success(request,"Product Added Succesfully")
    
    return render(request,'seller_interface.html')

def login(request):

    if request.method=="POST":

        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username)
        print(password)

        hey=Signup.objects.filter(first_name=username).exists()

        print(hey)
        if hey==True:
            return redirect('seller_interface')
            
    return render(request,'login.html')


def login_buy(request):
    if request.method=="POST":

        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username)
        print(password)

        hey=Signup.objects.filter(first_name=username).exists()

        print(hey)
        if hey==True:
            return redirect('buyer_interface')
        else:
            return render(request,'login_buy.html')
    else:
        return render(request,'login_buy.html')
    
def adm(request):
    all=Item.objects.all()
    con={'Show':all}
    return render(request,'adm.html',con)
def buyer_interface(request):
    alldata=Item.objects.all()
    context={'Images':alldata}

    print(context)

    return render(request,'buyer_interface.html',context)

def update(request,id):
    mymember = Item.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'mymember': mymember,
    }
    return render(request,'update.html',context)


def updaterecord(request, id):
  first = request.POST['bid_amt']
  bidder=request.POST['bidder']
  member = Item.objects.get(id=id)
  member.price = first
  member.current_bidder_name=bidder
  member.save()
  return HttpResponseRedirect(reverse('buyer_interface'))

def home(request):
    return render(request,'home.html')