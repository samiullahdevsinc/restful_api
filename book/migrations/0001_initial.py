# Generated by Django 4.1.4 on 2023-08-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
