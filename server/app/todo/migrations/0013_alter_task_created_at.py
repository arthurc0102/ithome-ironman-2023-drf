# Generated by Django 4.2.5 on 2023-10-11 14:54

from django.db import migrations

import server.utils.models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0012_alter_task_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=server.utils.models.CreatedAtField(auto_now_add=True),
        ),
    ]