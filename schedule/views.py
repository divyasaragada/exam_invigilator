from django.shortcuts import render,redirect
from django.contrib import messages

from django.http import HttpResponse 
from schedule.models import faculty,room,exam,student,number,adminlogin,conduct

def home(request):
	
	return render(request,'schedule/home.html')

def admin1(request):
	if request.method=="POST":
		uname=request.POST['uname']
		passwd=request.POST['password']
		
		try:
			data=adminlogin.objects.get(username=uname,password=passwd)
			if data:
				
				return render(request,'schedule/adminpage.html')
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
	
	data=conduct.objects.select_related('ex','fna1','room').all()
	return render(req,'schedule/timetable.html',{'data':data})

from django.contrib.auth.decorators import login_required

@login_required
def adminpage(request):
	return render(request,'schedule/adminpage.html')


def addexam(request):
	if request.method=='POST':
		i=request.POST['id']
		date=request.POST['date']
		time=request.POST['time']
		try:
			data=exam.objects.create(id=i,exam_date=date,exam_time=time)
			return render(request,'schedule/addexam.html')
	
		except Exception:
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'schedule/addexam.html')
		
	return render(request,'schedule/addexam.html')

def assignfac(request):
	if request.method=="POST":
		i=request.POST['id']
		fname=request.POST['fname']
		ro=request.POST['room']
		sem=request.POST['sem']
		sub=request.POST['sub']
		dept=request.POST['dept']
		try:
			exobj=exam.objects.get(id=i)
			r=room.objects.get(roomno=ro)
			x=faculty.objects.get(fname=fname)
			data=conduct.objects.create(fna1=x,ex=exobj,room=r,semester=sem,dept=dept,subject=sub)
		
		except Exception:
			messages.info(request,'Please enter all the required details!!!.......')
			return render(request,'schedule/assignfac.html')
	data1=exam.objects.all()
	
	data3=room.objects.filter(room_status='y')
	dx=conduct.objects.all().values('fna1')
	dy=faculty.objects.exclude(fname__in=dx)
	return render(request,'schedule/assignfac.html',{'x':data1,'y':dy,'z':data3})
