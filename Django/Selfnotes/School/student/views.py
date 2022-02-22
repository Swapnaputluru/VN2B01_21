from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
@csrf_exempt
def create_details(request):
    details=Mark()
    details.Student_name = request.POST.get('Student_name')
    details.Student_id = request.POST.get('Student_id')
    details.Telugu_marks = request.POST.get('Telugu_marks')
    details.English_marks = request.POST.get('English_marks')
    details.kannada_marks = request.POST.get('kannada_marks')
    details.Hindi_marks = request.POST.get('Hindi_marks')
    details.Maths_marks = request.POST.get('Maths_marks')
    details.Science_marks = request.POST.get('Science_marks')
    details.save()
    #StudentMark.objects.create(details)
    return render(request, "student/form.html")
    #return HttpResponse("successfully created")

    #list=['Student_name', 'Student_id', 'Telugu_marks', '', '', ]
    #StudentMark.objects.create(Student_name= details.Student_name,Student_id=details.Student_id,Telugu_marks=details.Telugu_marks,English_marks=details.English_marks,kannada_marks=details.kannada_marks,Hindi_marks=details.Hindi_marks,Maths_marks=details.Maths_marks , Science_marks=details.Science_marks)
    #StudentMark.objects.create(Student_name=Student_name, Student_id=Student_id  ,Telugu_marks  = Telugu_marks , English_marks =English_marks  , kannada_marks = kannada_marks ,  =  ,  =  ,  =  ,  =  ,  =  , )
    #return HttpResponse(f'{details.Student_name} {details.Student_id}  {details.Telugu_marks} {details.English_marks} {details.kannada_marks} {details.Hindi_marks} {details.Maths_marks} {details.Science_marks}')



def delete(request,student_id):
    try:
        object = Mark.objects.get(pk=student_id)
        object.delete()
        return HttpResponse("Successfully deleted")
    except:
        return HttpResponse("not found")


def retrieve(request):
    data = Mark.objects.all()
    return render(request,"student/retrieve.html",{"data": data})
'''
def update(request,data,Student_id):
    try:
        object=Mark.objects.get(id=Student_id)
        object.update(data)
        return HttpResponse("Update successful")
    except:
        return HttpResponse("Update unsuccessful")

'''

