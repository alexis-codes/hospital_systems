# Generated by Django 5.1.6 on 2025-02-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0005_rename_apointment_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
