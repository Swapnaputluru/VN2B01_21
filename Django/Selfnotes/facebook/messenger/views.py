from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
def demo_fun(request):
    return HttpResponse("Hello Swapna!!!!!!!!!!!!!!")


def demo_fun1(request, city):
    return HttpResponse(f"Welcome to the city {city}")


def demo_rend1(request):
   return render(request, 'messenger/index.html')

def demo_rend3(request):
    s_no = [1, 2, 3, 4, 5]
    courses = ("Python", ".Net","Java", "Power bi", "Sales force")
    data = {'key_s_no': s_no, 'key_courses': courses}
    return render(request, "messenger/group.html", data)


def home(request):
    html="please <a href=getdata>Enter name here</a>"
    return HttpResponse(html)

def getdata(request):
   return render(request, 'messenger/check.html')

def showResult(request):
    nm1= request.GET['fname']
    nm2= request.GET['lname']
    nm = nm1+' '+nm2
    return render(request,'messenger/showResult.html', {'name':nm})

@csrf_exempt
def post_method(request):
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse(f'hello my {name} is {id} ')


def demo_rend2(request, name, id):
    data = {'key_name' : name, 'key_id' : id}
    Data.objects.create(name=name,id=id)
    return render(request,"messenger/parameters.html", data)

@csrf_exempt
def post_method1(request):
    location = request.POST["location"]
    state = request.POST["state"]
    Adddetails.objects.create(location=location,state = state)
    return HttpResponse(f'my locotion {location} and state {state}')



'''
def home(request):
    html="please <a href=getdata>Enter name here</a>"
    return HttpResponse(html)

def getdata(request):
   return render(request, 'messenger/check.html')

def showResult(request):

    nm1= request.POST['fname']
    nm2= request.POST['lname']
    nm = nm1+' '+nm2
    return render(request,'messenger/showResult.html', {'name':nm})

'''
