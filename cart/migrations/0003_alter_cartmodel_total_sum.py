# Generated by Django 4.1.3 on 2022-12-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartmodel_total_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='total_sum',
            field=models.IntegerField(default=0),
        ),
    ]