# Generated by Django 3.2.7 on 2021-11-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20211011_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
