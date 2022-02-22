from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.create_details, name= 'student details'),
    path('del/<int:student_id>', views.delete, name= 'student details'),
    path('retrieve/', views.retrieve, name= 'student details'),
    #path('update/<int:student_id>/<int:data>', views.update, name= 'student details'),
]