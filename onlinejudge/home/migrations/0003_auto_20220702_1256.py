# Generated by Django 2.2 on 2022-07-02 07:26

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220629_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
