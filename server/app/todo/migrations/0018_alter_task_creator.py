# Generated by Django 4.2.5 on 2023-10-13 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todo", "0017_set_creator_to_tasks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
