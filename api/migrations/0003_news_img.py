# Generated by Django 4.1.1 on 2023-02-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(default=1, upload_to='news/'),
            preserve_default=False,
        ),
    ]
