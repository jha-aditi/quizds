# Generated by Django 3.0.6 on 2020-05-08 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, unique=True)),
                ('question', models.CharField(max_length=500)),
                ('islink', models.BooleanField(default=False)),
                ('ispic', models.BooleanField(default=False)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, unique=True)),
                ('question', models.CharField(max_length=500)),
                ('islink', models.BooleanField(default=False)),
                ('ispic', models.BooleanField(default=False)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Myusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=30)),
                ('pointsfactor', models.IntegerField(default=0)),
                ('lastcorrectans', models.DateTimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]