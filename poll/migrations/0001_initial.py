# Generated by Django 5.1.2 on 2024-10-30 01:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='publish date')),
            ],
        ),
        migrations.CreateModel(
            name='Question_choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('vote', models.IntegerField(default=0)),
                ('question_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='poll.question')),
            ],
        ),
    ]
