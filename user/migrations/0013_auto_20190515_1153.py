# Generated by Django 2.2.1 on 2019-05-15 11:53

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20190515_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profileimage/goat.jpg', storage=django.core.files.storage.FileSystemStorage(location='/media/profileimage'), upload_to='profileimage/'),
        ),
    ]
