# Generated by Django 5.1.5 on 2025-02-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_buisnesuser_companie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
