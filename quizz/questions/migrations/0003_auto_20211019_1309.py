# Generated by Django 3.2.8 on 2021-10-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='question',
            name='time_asked',
            field=models.IntegerField(default=0),
        ),
    ]
