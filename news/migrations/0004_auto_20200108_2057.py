# Generated by Django 2.2.2 on 2020-01-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200108_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(related_name='news_categories', to='news.Category'),
        ),
    ]
