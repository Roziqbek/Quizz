# Generated by Django 4.1.7 on 2023-04-28 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
