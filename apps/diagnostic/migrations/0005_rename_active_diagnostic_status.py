# Generated by Django 4.1.3 on 2023-03-21 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0004_alter_diagnostic_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnostic',
            old_name='active',
            new_name='status',
        ),
    ]
