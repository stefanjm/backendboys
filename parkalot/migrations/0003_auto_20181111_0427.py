# Generated by Django 2.1.3 on 2018-11-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkalot', '0002_auto_20181111_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
