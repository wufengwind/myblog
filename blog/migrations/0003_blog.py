# Generated by Django 2.0 on 2019-08-20 07:49

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_essay_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容\t')),
            ],
        ),
    ]
