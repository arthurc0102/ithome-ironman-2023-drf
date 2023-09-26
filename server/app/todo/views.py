from rest_framework import viewsets

from server.app.todo import models as todo_models
from server.app.todo import serializers as todo_serializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = todo_models.Task.objects.all()
    serializer_class = todo_serializers.TaskSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return todo_serializers.TaskCreateSerializer

        return super().get_serializer_class()


class TagViewSet(viewsets.ModelViewSet):
    queryset = todo_models.Tag.objects.all()
    serializer_class = todo_serializers.TagSerializer
