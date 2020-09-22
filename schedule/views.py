from django.shortcuts import render,redirect

from django.http import HttpResponse 
from schedule.models import faculty,room,exam,student,number,adminlogin

def home(req):
	return render(req,'schedule/home.html')
def timetable(req):
	data=room.objects.filter(room_status='y')
	return render(req,'schedule/timetable.html',{'data':data})
