# Generated by Django 4.1 on 2022-09-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_alter_article_body_alter_matchreport_burnley_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_snippet',
            field=models.CharField(default='null', max_length=115),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.CharField(max_length=340),
        ),
    ]
