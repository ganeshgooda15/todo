# Generated by Django 4.0.4 on 2022-09-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_deleted',
            field=models.CharField(default='n', max_length=2),
        ),
    ]
