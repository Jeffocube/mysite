# Generated by Django 3.0.7 on 2020-06-20 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20200619_0437'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Greeting',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
