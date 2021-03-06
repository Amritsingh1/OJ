# Generated by Django 2.2 on 2022-06-29 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.IntegerField()),
                ('statement', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], max_length=6)),
                ('input', models.TextField(default='')),
                ('output', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_id', models.IntegerField()),
                ('verdict', models.CharField(max_length=12)),
                ('datetime', models.DateTimeField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problems')),
            ],
        ),
    ]
