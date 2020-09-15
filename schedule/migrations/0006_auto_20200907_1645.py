# Generated by Django 3.0.8 on 2020-09-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_examinvigilator_duties'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50, unique=True)),
                ('faculty_id', models.IntegerField(unique=True)),
                ('exam_date', models.DateField()),
                ('exam_time', models.CharField(max_length=50)),
                ('roomno', models.IntegerField()),
                ('exam_type', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('1-1', '1-1'), ('1-2', '1-2'), ('2-1', '2-1'), ('2-2', '2-2')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('faculty_name', models.CharField(max_length=50)),
                ('faculty_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('faculty_status', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('dept', models.CharField(choices=[('it', 'information technology'), ('eee', 'electrical'), ('cse', 'computer science'), ('ece', 'electronics and communication')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('roomno', models.IntegerField(primary_key=True, serialize=False)),
                ('roomcapacity', models.IntegerField()),
                ('room_status', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('rollno', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_dept', models.CharField(choices=[('it', 'information technology'), ('eee', 'electrical'), ('cse', 'computer science'), ('ece', 'electronics and communication')], max_length=3)),
                ('year', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
            ],
        ),
        migrations.DeleteModel(
            name='examinvigilator_duties',
        ),
    ]
