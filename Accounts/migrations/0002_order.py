# Generated by Django 4.0 on 2021-12-25 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Rests', '0005_alter_cat_image'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('content', models.ManyToManyField(blank=True, to='Rests.Meal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
        ),
    ]
