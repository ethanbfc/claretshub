# Generated by Django 4.1 on 2022-09-30 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='administrator',
            new_name='writer',
        ),
    ]
