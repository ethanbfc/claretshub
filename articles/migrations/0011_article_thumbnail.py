# Generated by Django 4.1 on 2022-08-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_body_alter_article_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
    ]