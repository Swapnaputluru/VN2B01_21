from django.urls import path

from .views import *

urlpatterns = [path(' ', demo_fun, name="Check"),
               path('type/<city>', demo_fun1,name="city"),
               path('demo1', demo_rend1,name = "demo"),
               path('p/<str:name>/<int:id>', demo_rend2,name = "name_id"),
               path('group/', demo_rend3,name = "group"),
               path('check', home, name="check"),
               path('getdata/', getdata, name="getdata"),
               path('getdata/showResult/', showResult,name='showresult'),
               path('post/', post_method, name='post'),
               path('post1/', post_method1, name='post1'),

               ]

#   path('type/<int:city>', views.demo_fun1),