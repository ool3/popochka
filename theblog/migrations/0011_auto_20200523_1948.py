# Generated by Django 3.0.6 on 2020-05-23 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
