# Generated by Django 4.1.3 on 2023-02-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorypet',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]