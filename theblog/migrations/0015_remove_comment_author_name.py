# Generated by Django 3.0.6 on 2020-06-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_auto_20200611_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_name',
        ),
    ]
