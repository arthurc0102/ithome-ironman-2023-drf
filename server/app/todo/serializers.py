from rest_framework import serializers

from server.app.todo import models as todo_models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo_models.Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = todo_models.Category
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

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=todo_models.Category.objects.all(),
        source="category",
    )

    creator_id = serializers.ReadOnlyField()

    class Meta:
        model = todo_models.Task
        exclude = ("creator",)


class TaskCreateSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        read_only_fields = ("is_finish",)
