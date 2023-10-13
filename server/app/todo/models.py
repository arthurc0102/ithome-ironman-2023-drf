from django.contrib import auth
from django.db import models

from server.utils import models as model_utils

User = auth.get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_finish = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    end_at = models.DateTimeField(null=True, blank=True)
    created_at = model_utils.CreatedAtField()
    updated_at = model_utils.UpdatedAtField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    attachment = models.FileField(blank=True, upload_to="task/attachments/")
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
