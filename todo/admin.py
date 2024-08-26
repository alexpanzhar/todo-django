from django.contrib import admin

from todo.models import Tag, Task

# Register your models here.
admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "datetime",
        "deadline",
        "is_done",
    )
    list_filter = ("tags",)
    search_fields = ("content",)
