# Generated by Django 4.1 on 2022-09-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_alter_article_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='banner',
            field=models.ImageField(default='default/default_banner.png', upload_to='images/'),
        ),
    ]
