# Generated by Django 5.1.6 on 2025-02-21 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=256, verbose_name='Password'),
        ),
    ]
