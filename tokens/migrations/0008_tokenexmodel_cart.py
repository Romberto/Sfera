# Generated by Django 4.1.3 on 2022-12-19 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0014_excursionphonecodmodel_human_count'),
        ('tokens', '0007_remove_tokenexmodel_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenexmodel',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='excursions.excursionphonecodmodel'),
        ),
    ]
