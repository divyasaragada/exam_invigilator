"""exam_invigilator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from schedule import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('first/',views.first,name='first'),
    path('feedback/',views.feedback,name='feedback'),
    path('timetable/',views.timetable,name='timetable'),

    path('admin1/',views.admin1,name='admin1'),
    path('fac/',views.fac,name='fac'),
    path('stud/',views.stud,name='stud'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('addexam/',views.addexam,name='addexam'),
    path('facstatus/',views.facstatus,name='facstatus'),
    path('roomstatus/',views.roomstatus,name='roomstatus'),
    path('assignfac/<int:exid>/',views.assignfac,name='assignfac'),
    path('addfac/',views.addfac,name='addfac'),
    path('addroom/',views.addroom,name='addroom'),

    path('delete/<int:cid>/',views.delete,name='delete'),
    path('update/<int:cid>',views.update,name="update"),
    path('dele/<int:exid>/',views.dele,name="dele"),

    path('timetable2/',views.timetable2,name='timetable2'),
    path('timetable3/',views.timetable3,name='timetable3'),
    path('timetable4/',views.timetable4,name='timetable4'),

    path('request/',views.request,name='request'),
    path('facstart/',views.facstart,name='facstart'),
    path('facconstraints',views.facconstraints,name='facconstraints'),
    path('delet/<int:id>/',views.delet,name="delet"),

     path('addtt',views.addtt,name="addtt"),
     path('deltt/<str:name>',views.deltt,name="deltt"),
     path('showtt/<str:name>/',views.showtt,name="showtt"),

     path('send_email/',views.send_email,name='send_email'),
     path('head1/',views.head1,name='head1'),
]

