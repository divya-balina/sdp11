# Generated by Django 5.0 on 2024-03-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managermodule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetails',
            name='no_of_rooms',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='type_of_room',
            field=models.TextField(max_length=255),
        ),
    ]
