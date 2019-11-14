# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-14 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.BooleanField()),
                ('score', models.IntegerField()),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile/')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='question/')),
                ('category', models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('Javascript', 'Javascript'), ('Angular', 'Angular'), ('Flask', 'Flask'), ('Django', 'Django'), ('Java', 'Java'), ('Android', 'Android')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='approved',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Profile'),
        ),
    ]
