# Generated by Django 5.0.6 on 2024-06-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_appointment_delete_drug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='address',
            new_name='p_address',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='datetime',
            new_name='p_date_time',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='email',
            new_name='p_email',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='p_name',
        ),
    ]
