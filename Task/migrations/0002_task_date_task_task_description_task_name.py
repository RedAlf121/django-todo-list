# Generated by Django 5.1.4 on 2024-12-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date task',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='task', max_length=200),
        ),
    ]