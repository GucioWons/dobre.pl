# Generated by Django 4.0 on 2021-12-25 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rests', '0003_alter_meal_rest_id_alter_rest_cat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='rest_id',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='rest',
            old_name='cat_id',
            new_name='category',
        ),
    ]
