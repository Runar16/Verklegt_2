# Generated by Django 2.2.1 on 2019-05-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='profile_picture',
        ),
    ]