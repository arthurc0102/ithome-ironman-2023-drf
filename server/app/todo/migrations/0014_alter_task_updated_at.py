# Generated by Django 4.2.5 on 2023-10-11 15:14

from django.db import migrations

import server.utils.models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0013_alter_task_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="updated_at",
            field=server.utils.models.UpdatedAtField(auto_now=True),
        ),
    ]