# Generated by Django 2.2.1 on 2019-05-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20190515_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profileimage/twitter_eggandgumdrop.0.jpg', upload_to='profileimage/'),
        ),
    ]
