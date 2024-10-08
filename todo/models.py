from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = (
            "is_done",
            "-datetime",
        )

    def __str__(self):
        return self.content
