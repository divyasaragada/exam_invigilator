# Generated by Django 3.0.8 on 2020-09-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0004_delete_examinvigilator_duties'),
    ]

    operations = [
        migrations.CreateModel(
            name='examinvigilator_duties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50)),
                ('faculty_id', models.IntegerField(null=True)),
                ('exam_date', models.DateField()),
                ('exam_time', models.CharField(max_length=50)),
                ('roomno', models.IntegerField()),
                ('exam_type', models.CharField(max_length=50)),
            ],
        ),
    ]
