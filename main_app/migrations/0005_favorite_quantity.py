# Generated by Django 5.1 on 2024-08-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
