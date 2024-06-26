# Generated by Django 3.2.8 on 2024-03-18 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_title', models.CharField(max_length=255)),
                ('note_desc', models.TextField()),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
