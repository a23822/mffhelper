# Generated by Django 4.1.1 on 2023-01-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=140)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
