# Generated by Django 4.1.3 on 2022-11-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcursionPhoneCodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('random_cod', models.IntegerField()),
            ],
        ),
    ]