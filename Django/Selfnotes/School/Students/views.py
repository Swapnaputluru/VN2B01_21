from django.shortcuts import render,HttpResponse


# Create your views here.
def create_details(request):
    Student_name=request.POST['Student_name']
    Student_id = request.POST['Student_id']
    Telugu_marks = request.POST['Telugu_marks']
    English_marks = request.POST['English_marks']
    kannada_marks = request.POST['kannada_marks']
    Hindi_marks = request.POST['Hindi_marks']
    Maths_marks = request.POST['Maths_marks']
    Science_marks = request.POST['Science_marks']
    #StudentMark.objects.create()
    return HttpResponse(f'{Student_name}',{Student_id}, {Telugu_marks}, {English_marks}, {kannada_marks},{Hindi_marks}, {Maths_marks}, {Science_marks})


