# Generated by Django 4.1.3 on 2022-12-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0004_alter_tokenexmodel_driver_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenexmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
