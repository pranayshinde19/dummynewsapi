# Generated by Django 4.1.1 on 2023-02-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]
