# Generated by Django 4.1.3 on 2022-11-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_alter_drivermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivermodel',
            name='password_hash',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='drivermodel',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
