# Generated by Django 3.0.8 on 2020-10-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20201028_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
