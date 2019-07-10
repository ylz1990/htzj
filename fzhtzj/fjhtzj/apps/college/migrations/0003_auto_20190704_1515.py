# Generated by Django 2.2 on 2019-07-04 15:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_expertcomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooperativeResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=150, verbose_name='标题')),
                ('image_url', models.ImageField(blank=True, default='', upload_to='img')),
                ('content', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now=True, help_text='发布时间', verbose_name='发布时间')),
            ],
            options={
                'verbose_name_plural': '合作资源',
                'db_table': 'CR_table',
                'ordering': ['-create_date', '-id'],
                'verbose_name': '合作资源',
            },
        ),
        migrations.CreateModel(
            name='DataCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=150, verbose_name='标题')),
                ('image_url', models.ImageField(blank=True, default='', upload_to='img')),
                ('content', tinymce.models.HTMLField()),
                ('create_date', models.DateTimeField(auto_now=True, help_text='发布时间', verbose_name='发布时间')),
            ],
            options={
                'verbose_name_plural': '数据中心',
                'db_table': 'DC_table',
                'ordering': ['-create_date', '-id'],
                'verbose_name': '数据中心',
            },
        ),
        migrations.AlterField(
            model_name='realtimenews',
            name='image_url',
            field=models.ImageField(blank=True, default='', upload_to='img'),
        ),
    ]
