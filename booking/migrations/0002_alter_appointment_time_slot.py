# Generated by Django 5.1.6 on 2025-03-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_slot',
            field=models.CharField(choices=[('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM')], max_length=10),
        ),
    ]
