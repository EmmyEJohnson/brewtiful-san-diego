# Generated by Django 3.2.9 on 2021-11-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0006_vendorprofile_company_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brew',
            options={},
        ),
        migrations.AddField(
            model_name='brew',
            name='brew_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ale'), (2, 'Lager'), (3, 'Lambic')], null=True),
        ),
        migrations.AddField(
            model_name='brew',
            name='brewery',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='brew',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='brew',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='brew',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
