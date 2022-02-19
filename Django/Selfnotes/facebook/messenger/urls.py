from django.urls import path

from . import views

urlpatterns = [path(' ', views.demo_fun, name="Check"),
               path('type/<city>', views.demo_fun1,name="city"),
               path('demo1', views.demo_rend1,name = "demo"),
               path('p/<str:name>/<int:id>', views.demo_rend2,name = "name_id"),
               path('group/', views.demo_rend3,name = "group"),
               path('check', views.home, name="check"),
               path('getdata/', views.getdata, name="getdata"),
               path('getdata/showResult/', views.showResult,name='showresult'),
               path('post/', views.post_method, name='post'),
               path('post1/', views.post_method1, name='post1'),
               ]

#   path('type/<int:city>', views.demo_fun1),