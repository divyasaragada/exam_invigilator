from django.db import models
from django.db.models import Model 

    
class faculty(models.Model):
	options=(('y',"yes"),('n','no'))
	depts=(('it','information technology'),('eee','electrical'),('cse','computer science'),('ece',"electronics and communication"))
	fname=models.CharField(primary_key=True,max_length=50,null=False,default='none')
	faculty_id=models.IntegerField()
	faculty_status=models.CharField(max_length=1,choices=options,default='y')
	email=models.EmailField()
	dept=models.CharField(max_length=3,choices=depts)

class room(models.Model):
	options=(('y',"yes"),('n','no'))
	roomno=models.IntegerField(primary_key=True)
	roomcapacity=models.IntegerField()
	room_status=models.CharField(max_length=1,choices=options,default='y')

class exam(models.Model):
	semesters = (("1-1","1-1"),("1-2","1-2"),("2-1","2-1"),("2-2","2-2"),("2-1","2-1"),("2-2","2-2"),("3-1","3-1"),("4-2","4-2"))
	depts=(('it','information technology'),('eee','electrical'),('cse','computer science'),('ece',"electronics and communication"))
	id=models.IntegerField(primary_key=True)
	exam_date=models.DateField(null=False)
	exam_time=models.CharField(max_length=50,null=False,default='none')

	semester=models.CharField(max_length=10,choices=semesters,default='3-1')
	dept=models.CharField(max_length=3,choices=depts,default='cse')	
	subject=models.CharField(max_length=50,default='none',null=False)

class conduct(models.Model):
	

	fna1=models.ForeignKey(faculty,on_delete=models.CASCADE)
	fna2=models.CharField(max_length=50,null=True)
	ex=models.ForeignKey(exam,on_delete=models.CASCADE)
	room=models.ForeignKey(room, on_delete=models.CASCADE)
	


class student(models.Model):
	x=((1,1),(2,2),(3,3),(4,4))
	depts=(('it','information technology'),('eee','electrical'),('cse','computer science'),('ece',"electronics and communication"))
	rollno=models.CharField(max_length=50,null=False,primary_key=True)
	student_name=models.CharField(max_length=50,null=False)
	stu_email=models.EmailField()
	stu_dept=models.CharField(max_length=3,choices=depts)
	year=models.IntegerField(choices=x)

class adminlogin(models.Model):
	username=models.CharField(max_length=50,null=False)
	password=models.CharField(max_length=50,null=False)

class constraints(models.Model):
	cname=models.CharField(max_length=50,null=False)
	cdate=models.DateField(null=False)
class tt(models.Model):
	depts=(('cse','CSE'),('it','IT'),('eee','EEE'),('ece',"ECE"))
	Schedule=models.ImageField(default='null')
	Section=models.CharField(max_length=50,null='False')
	Branch=models.CharField(max_length=5,choices=depts)
class feed(models.Model):
	name=models.CharField(max_length=50,null=False)
	email=models.EmailField(null=True)
	feedback=models.CharField(max_length=1000)
class head(models.Model):
	heading=models.CharField(max_length=1000,default='EXAM TIMETABLE')

	





