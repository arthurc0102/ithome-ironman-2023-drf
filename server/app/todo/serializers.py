from rest_framework import serializers

from server.app.todo import models as todo_models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo_models.Task
        fields = "__all__"
