from django.db import models
from django.db.models import Model 

    
class faculty(models.Model):
	options=(('y',"yes"),('n','no'))
	depts=(('it','information technology'),('eee','electrical'),('cse','computer science'),('ece',"electronics and communication"))
	faculty_name=models.CharField(max_length=50,null=False)
	faculty_id=models.IntegerField(primary_key=True)
	faculty_status=models.CharField(max_length=1,choices=options)
	email=models.EmailField()
	dept=models.CharField(max_length=3,choices=depts)

class room(models.Model):
	options=(('y',"yes"),('n','no'))
	roomno=models.IntegerField(primary_key=True)
	roomcapacity=models.IntegerField()
	room_status=models.CharField(max_length=1,choices=options)


class exam(models.Model):
	semesters = (("1-1","1-1"),("1-2","1-2"),("2-1","2-1"),("2-2","2-2"),("2-1","2-1"),("2-2","2-2"),("3-1","3-1"),("4-2","4-2"))
	faculty_name=models.CharField(max_length=50,null=False)
	faculty_id=models.ForeignKey(faculty, on_delete=models.CASCADE)
	exam_date=models.DateField(null=False)
	exam_time=models.CharField(max_length=50,null=False)
	roomno=models.ForeignKey(room, on_delete=models.CASCADE)
	exam_type=models.CharField(max_length=50,null=False)
	semester=models.CharField(max_length=10,choices=semesters)	


class student(models.Model):
	x=((1,1),(2,2),(3,3),(4,4))
	depts=(('it','information technology'),('eee','electrical'),('cse','computer science'),('ece',"electronics and communication"))
	rollno=models.CharField(max_length=50,null=False,primary_key=True)
	student_name=models.CharField(max_length=50,null=False)
	stu_email=models.EmailField()
	stu_dept=models.CharField(max_length=3,choices=depts)
	year=models.IntegerField(choices=x)





