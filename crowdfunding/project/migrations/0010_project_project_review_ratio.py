# Generated by Django 4.1.1 on 2022-09-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_project_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_review_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]