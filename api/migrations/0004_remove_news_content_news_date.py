# Generated by Django 4.1.1 on 2023-02-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_news_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
