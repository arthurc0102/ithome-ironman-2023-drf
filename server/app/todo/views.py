from rest_framework import authentication, decorators, permissions, response, viewsets

from server.app.todo import models as todo_models
from server.app.todo import serializers as todo_serializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = todo_models.Task.objects.all()
    serializer_class = todo_serializers.TaskSerializer

    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "create":
            return todo_serializers.TaskCreateSerializer

        return super().get_serializer_class()

    @decorators.action(methods=["patch"], detail=True)
    def status(self, request, pk):
        task = self.get_object()

        serializer = self.get_serializer(
            task,
            data={"is_finish": not task.is_finish},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = todo_models.Tag.objects.all()
    serializer_class = todo_serializers.TagSerializer
