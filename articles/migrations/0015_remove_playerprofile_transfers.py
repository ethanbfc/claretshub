# Generated by Django 4.1 on 2022-08-24 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_matchreport_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerprofile',
            name='transfers',
        ),
    ]
