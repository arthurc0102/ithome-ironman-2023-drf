# Generated by Django 4.2.5 on 2023-10-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0004_task_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]