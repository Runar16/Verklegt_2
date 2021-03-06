# Generated by Django 2.2.1 on 2019-05-06 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.CharField(max_length=10)),
                ('property_description', models.CharField(max_length=2000)),
                ('zip', models.CharField(max_length=10)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('size', models.IntegerField()),
                ('rooms', models.IntegerField(blank=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property')),
            ],
        ),
    ]
