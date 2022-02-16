from django.shortcuts import render
from django.http import HttpResponse
import re
def demo_fun(request):
    return HttpResponse("Hello Swapna!!!!!!!!!!!!!!")


def demo_fun1(request, city):
    return HttpResponse(f"Welcome to the city {city}")


def demo_rend1(request):
   return render(request, 'messenger/index.html')


def demo_rend2(request, name, id):
    data = {'key_name' : name, 'key_id' : id}
    return render(request, "messenger/parameters.html", data)


def demo_rend3(request):
    s_no = [1, 2, 3, 4, 5]
    courses = ["Python", ".Net","Java", "Power bi", "Sales force"]
    data = {'key_s_no': s_no, 'key_courses': courses}
    return render(request, "messenger/group.html", data)
