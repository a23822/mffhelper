# Generated by Django 4.1.1 on 2023-01-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='charIndex',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='hero',
            name='latestUniform',
            field=models.BooleanField(default=False),
        ),
    ]
