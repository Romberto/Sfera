# Generated by Django 4.1.3 on 2022-12-22 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_cod', '0002_productcodmodel_count_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcodmodel',
            name='count_tokens',
        ),
    ]
