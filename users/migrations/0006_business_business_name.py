# Generated by Django 5.0.6 on 2024-06-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_contact_alter_profile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
