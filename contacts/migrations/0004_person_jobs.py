# Generated by Django 3.0.5 on 2020-05-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
        ('contacts', '0003_auto_20200502_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='jobs',
            field=models.ManyToManyField(through='contacts.Interaction', to='jobs.Job'),
        ),
    ]