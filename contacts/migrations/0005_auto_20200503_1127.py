# Generated by Django 3.0.5 on 2020-05-03 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_person_jobs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interaction',
            options={'get_latest_by': 'created_at'},
        ),
    ]
