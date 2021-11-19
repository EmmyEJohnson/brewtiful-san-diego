# Generated by Django 3.2.9 on 2021-11-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorprofile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='town',
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='post_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Zip Code'),
        ),
    ]