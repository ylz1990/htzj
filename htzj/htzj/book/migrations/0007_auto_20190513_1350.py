# Generated by Django 2.2 on 2019-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20190510_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='new_type',
            field=models.CharField(default="['新闻资讯']", max_length=10),
        ),
    ]
