# Generated by Django 5.1.1 on 2024-09-11 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceClient',
            new_name='Client',
        ),
    ]
