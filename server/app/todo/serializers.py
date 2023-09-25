from rest_framework import serializers

from server.app.todo import models as todo_models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo_models.Tag
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        allow_empty=False,
        write_only=True,
        many=True,
        queryset=todo_models.Tag.objects.all(),
        source="tags",
    )

    class Meta:
        model = todo_models.Task
        fields = "__all__"
