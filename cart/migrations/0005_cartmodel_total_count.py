# Generated by Django 4.1.3 on 2022-12-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartitemmodel_count_alter_cartmodel_total_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='total_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
