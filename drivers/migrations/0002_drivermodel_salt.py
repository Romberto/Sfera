# Generated by Django 4.1.3 on 2022-11-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivermodel',
            name='salt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
