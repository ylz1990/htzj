# Generated by Django 2.2 on 2019-05-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
