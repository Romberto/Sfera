# Generated by Django 4.1.3 on 2022-12-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_cod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcodmodel',
            name='count_tokens',
            field=models.IntegerField(default=0),
        ),
    ]
