# Generated by Django 5.0.6 on 2024-07-06 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_business_email_alter_business_barangay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='barangay',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='business_name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='municipality',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default=1, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='province',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Business',
        ),
    ]
