from django.db import models
from django_filters import rest_framework as filters

from server.app.todo import models as todo_models


class TagFilter(filters.FilterSet):
    has_task = filters.BooleanFilter(method="has_task_filter")
    task_count = filters.NumberFilter(method="task_count_filter")

    class Meta:
        model = todo_models.Tag
        fields = {
            "id": ("gt", "gte", "lt", "lte"),
            "name": ("exact", "contains", "icontains"),
        }

    def has_task_filter(self, queryset, name, value):
        qs = queryset.alias(task_count=models.Count("task"))

        if value:
            return qs.filter(task_count__gt=0)

        return qs.filter(task_count=0)

    def task_count_filter(self, queryset, name, value):
        return queryset.alias(task_count=models.Count("task")).filter(task_count=value)
