from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm
from todo.models import Task, Tag


# Create your views here.


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_form.html"

    form_class = TaskForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_form.html"

    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_confirm_delete.html"


class TaskToggleStatusView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:task-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_confirm_delete.html"
