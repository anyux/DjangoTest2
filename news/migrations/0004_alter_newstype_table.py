# Generated by Django 4.2.5 on 2024-11-23 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_options_alter_newstype_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='newstype',
            table='type',
        ),
    ]