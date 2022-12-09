# Generated by Django 4.1.3 on 2022-11-25 11:55

from django.db import migrations, models
import excursions.models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0003_excursionphonecodmodel_excursions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcursionPointModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.FileField(blank=True, null=True, upload_to=excursions.models.content_excursion_name)),
            ],
        ),
        migrations.AddField(
            model_name='excursionmodel',
            name='point',
            field=models.ManyToManyField(blank=True, null=True, to='excursions.excursionpointmodel'),
        ),
    ]