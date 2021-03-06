# Generated by Django 2.2.8 on 2019-12-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authro',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
