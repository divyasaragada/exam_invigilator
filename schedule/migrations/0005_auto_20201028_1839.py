# Generated by Django 3.0.8 on 2020-10-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20201017_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='tt',
            old_name='btt',
            new_name='Schedule',
        ),
        migrations.RenameField(
            model_name='tt',
            old_name='bname',
            new_name='Section',
        ),
        migrations.RemoveField(
            model_name='tt',
            name='branch',
        ),
        migrations.AddField(
            model_name='tt',
            name='Branch',
            field=models.CharField(default='CSE', max_length=5),
        ),
    ]
