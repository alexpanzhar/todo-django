from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task


# Create your views here.

class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_form.html"

    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_form.html"

    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_confirm_delete.html"
