# Generated by Django 5.0.6 on 2024-07-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_business_barangay_business_municipality_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='email',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='barangay',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='municipality',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='province',
            field=models.TextField(blank=True),
        ),
    ]
