# Generated by Django 5.1.5 on 2025-03-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='digital_book',
            field=models.BooleanField(default=False),
        ),
    ]
