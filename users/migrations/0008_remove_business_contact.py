# Generated by Django 5.0.6 on 2024-07-06 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_age_remove_profile_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='contact',
        ),
    ]
