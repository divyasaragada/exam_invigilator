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
		data=adminlogin.objects.get(username=uname,password=passwd)
		try:
			if data:
				d=exam.objects.all()
				return render(request,'schedule/adminpage.html',{'data':d})
		
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

def delete(request,cid):
	d=conduct.objects.get(id=cid)
	d.delete()
	data=conduct.objects.select_related('ex','fna1','room').all()
	return render(request,'schedule/timetable.html',{'data':data})

def timetable(request):
	
	data=conduct.objects.select_related('ex','fna1','room').all()
	return render(request,'schedule/timetable.html',{'data':data})

from django.contrib.auth.decorators import login_required

def adminpage(request):
	d=exam.objects.all()
	if request.method=='POST':
		exid=request.POST['id']

		try:
			d1=exam.objects.get(id=exid)
			if d1:
				data3=room.objects.filter(room_status='y')
				s=conduct.objects.filter(ex=d1).values('fna1')
				dy=faculty.objects.filter(faculty_status='y').exclude(fname__in=s)
				return render(request,'schedule/assignfac.html',{'x':d1,'y':dy,'z':data3})
		except Exception:
			messages.warning(request,'Please provide valid exam ID..or go to create exam for new exam..!')
			
			return render(request,'schedule/adminpage.html',{'data':d})
	
	return render(request,'schedule/adminpage.html',{'data':d})
	


def addexam(request):
	data=exam.objects.all()
	if request.method=='POST':
		i=request.POST['id']
		date=request.POST['date']
		time=request.POST['time']
		try:
			data=exam.objects.create(id=i,exam_date=date,exam_time=time)
			data=exam.objects.all()

			return render(request,'schedule/addexam.html',{'data':data})
	
		except Exception:
			data=exam.objects.all()
			messages.warning(request,'Please enter valid details!!!.......')
			return render(request,'schedule/addexam.html',{'data':data})
		
	return render(request,'schedule/addexam.html',{'data':data})


def dele(request,exid):
	d=exam.objects.get(id=exid)
	d.delete()
	data=exam.objects.all()
	return render(request,'schedule/addexam.html',{'data':data})
      

def assignfac(request,exid):
	if request.method=="POST":
		i=exid
		fname=request.POST['fname']
		f=request.POST['fna2']
		ro=request.POST['room']
		sem=request.POST['sem']
		sub=request.POST['sub']
		dept=request.POST['dept']
		exobj=exam.objects.get(id=i)
		r=room.objects.get(roomno=ro)
		x=faculty.objects.get(fname=fname)
		data=conduct.objects.create(fna1=x,ex=exobj,fna2=f,room=r,semester=sem,dept=dept,subject=sub)

		d1=exam.objects.get(id=exid)
		s1=conduct.objects.filter(ex=d1).values('fna1')
		s2=conduct.objects.filter(ex=d1).values('room')
		dy=faculty.objects.filter(faculty_status='y').exclude(fname__in=s1)
		data3=room.objects.filter(room_status='y').exclude(roomno__in=s2)
		s3=conduct.objects.filter(ex=d1).values('fna2')
		dz=dy.exclude(fname__in=s3)

		return render(request,'schedule/assignfac.html',{'x':d1,'y':dz,'z':data3})

	
		
		# except Exception:
		# 	messages.info(request,'Please enter all the required details!!!.......')
		# 	return render(request,'schedule/addexam.html')
	
	d1=exam.objects.get(id=exid)
	s1=conduct.objects.filter(ex=d1).values('fna1')
	s2=conduct.objects.filter(ex=d1).values('room')
	dy=faculty.objects.filter(faculty_status='y').exclude(fname__in=s1)
	data3=room.objects.filter(room_status='y').exclude(roomno__in=s2)

	s3=conduct.objects.filter(ex=d1).values('fna2')
	dz=dy.exclude(fname__in=s3)
	return render(request,'schedule/assignfac.html',{'x':d1,'y':dz,'z':data3})

def facstatus(request):
	if request.method=="POST":
		i=request.POST['id']
		d=faculty.objects.get(faculty_id=i)
		if(d.faculty_status=='y'):
			d.faculty_status='n'
		else:
			d.faculty_status='y'
		d.save()
		data=faculty.objects.all()
		return render(request,'schedule/facultyStatus.html',{'data':data})
	data=faculty.objects.all()
	return render(request,'schedule/facultyStatus.html',{'data':data})
def roomstatus(request):
	if request.method=="POST":
		i=request.POST['id']
		d=room.objects.get(roomno=i)
		if(d.room_status=='y'):
			d.room_status='n'
		else:
			d.room_status='y'
		d.save()
		data=room.objects.all()
		return render(request,'schedule/roomstatus.html',{'data':data})
	data=room.objects.all()
	return render(request,'schedule/roomstatus.html',{'data':data})

def addfac(request):
	if request.method=="POST":
		fname=request.POST['fname']
		fid=request.POST['fid']
		fmail=request.POST['fmail']
		fdept=request.POST['fdept']
		st=request.POST['st']
		try:
			data=faculty.objects.create(fname=fname,faculty_id=fid,email=fmail,dept=fdept,faculty_status=st)
			return render(request,'schedule/addfac.html')
		except Exception:
			messages.warning(request,'Please enter all details!!!.......')
			return render(request,'schedule/addfac.html')
	return render(request,'schedule/addfac.html')


def addroom(request):
	if request.method=="POST":
		fname=request.POST['rno']
		fid=request.POST['rcd']
		st=request.POST['st']
		try:
			data=room.objects.create(roomno=fname,roomcapacity=fid,room_status=st)
			return render(request,'schedule/addroom.html')
		except Exception:
			messages.warning(request,'Please enter all details!!!.......')
			return render(request,'schedule/addroom.html')
	return render(request,'schedule/addroom.html')
def update(request,cid):
	data=conduct.objects.get(id=cid)
	
	if request.method=="POST":
		i=data.id
		fe=request.POST['fname']
		f=request.POST['fna2']
		ro=request.POST['room']
		sem=request.POST['sem']
		sub=request.POST['sub']
		dept=request.POST['dept']

		data=conduct.objects.select_related('ex','fna1','room').get(id=i)
		data.subject=sub
		data.dept=dept
		data.semester=sem
		r=room.objects.get(roomno=ro)
		x=faculty.objects.get(fname=fe)
		data.fna2=f
		data.fna1=x
		data.room=r
		data.save()

		data1=conduct.objects.select_related('ex','fna1','room').all()
		return render(request,'schedule/timetable.html',{'data':data1})

	
	d1=exam.objects.get(id=data.ex.id)
	s1=conduct.objects.filter(ex=d1).values('fna1')
	s2=conduct.objects.filter(ex=d1).values('room')
	dy=faculty.objects.filter(faculty_status='y').exclude(fname__in=s1)
	data3=room.objects.filter(room_status='y').exclude(roomno__in=s2)

	s3=conduct.objects.filter(ex=d1).values('fna2')
	dz=dy.exclude(fname__in=s3)
	return render(request,'schedule/edit.html',{'data':data,'x':d1,'y':dz,'z':data3})

