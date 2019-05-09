# Generated by Django 2.2.1 on 2019-05-09 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_ssn', models.CharField(max_length=10)),
                ('sold_street_name', models.CharField(max_length=255)),
                ('sold_street_number', models.CharField(max_length=10)),
                ('realtor_licence_num', models.IntegerField(blank=True)),
                ('sold_zip', models.CharField(max_length=10)),
                ('sale_date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sold_property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Property')),
            ],
        ),
    ]