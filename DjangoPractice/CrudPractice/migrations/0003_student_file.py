# Generated by Django 3.1.3 on 2021-02-22 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CrudPractice', '0002_auto_20210211_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]