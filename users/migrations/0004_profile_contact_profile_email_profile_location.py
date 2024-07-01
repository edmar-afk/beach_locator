# Generated by Django 5.0.6 on 2024-06-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
