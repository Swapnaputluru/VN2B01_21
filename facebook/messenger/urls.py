from django.urls import path

from . import views

urlpatterns = [path('', views.demo_fun, name="Check"),
               path('type/<city>', views.demo_fun1),
               path('render_path/', views.demo_rend1),
               path('p/<str:name>/<int:id>', views.demo_rend2),
               path('group/', views.demo_rend3),
               ]

'''
{% for name in keynames %}
{{name}}
{% end for %} {% if {{key_id [0]}}==1 %}
you are match

{% end if %}
'''
#   path('type/<int:city>', views.demo_fun1),