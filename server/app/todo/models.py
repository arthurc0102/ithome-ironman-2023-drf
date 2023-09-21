from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_finish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
