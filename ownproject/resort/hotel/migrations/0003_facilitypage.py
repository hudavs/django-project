# Generated by Django 4.0.6 on 2022-11-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_roomies_alter_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='facilitypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('bookno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
