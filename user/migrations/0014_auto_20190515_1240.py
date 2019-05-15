# Generated by Django 2.2.1 on 2019-05-15 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20190515_1227'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0013_auto_20190515_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ssn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'property')},
            },
        ),
    ]