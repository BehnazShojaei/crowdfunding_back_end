# Generated by Django 5.1 on 2025-01-18 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_image_b64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]