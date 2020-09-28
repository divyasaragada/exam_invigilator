from django.shortcuts import render,redirect
from django.contrib import messages

from django.http import HttpResponse 
from schedule.models import faculty,room,exam,student,number,adminlogin

def home(request):
	
	return render(request,'schedule/home.html')

def admin1(request):
	if request.method=="POST":
		uname=request.POST['uname']
		passwd=request.POST['password']
		
		try:
			data=adminlogin.objects.get(username=uname,password=passwd)
			if data:
				messages.success(request,"logged in successfully!!..")
				return render(request,'schedule/admin.html')
		except Exception:
			#return HttpResponse("please enter correct details...!!!")

			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'schedule/admin.html')
			

	return render(request,'schedule/admin.html')


def fac(request):
	if request.method=="POST":
		id1=request.POST['id']
		email=request.POST['email']
		dept=request.POST['uname']
		try:
			data=faculty.objects.get(faculty_id=id1,email=email,dept=dept)
			if data:
				messages.success(request,"logged in successfully!!..")
				return render(request,'schedule/faculty.html')
		except Exception:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'schedule/faculty.html')


	return render(request,'schedule/faculty.html')

def stud(request):
	if request.method=="POST":
		uname=request.POST['uname']
		rno=request.POST['rno']
		
		try:
			data=student.objects.get(student_name=uname,rollno=rno)
			if data:
				messages.success(request,"logged in successfully!!..")
				return render(request,'schedule/student.html')
		except Exception:
			#return HttpResponse("please enter correct details...!!!")

			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'schedule/student.html')
			

	return render(request,'schedule/student.html')



def timetable(req):
	data=room.objects.filter(room_status='y')
	return render(req,'schedule/timetable.html',{'data':data})
