# Generated by Django 4.0 on 2021-12-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='adres',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
