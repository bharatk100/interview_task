from django.urls import path
from .views import TaskView

urlpatterns = [
    path("create", TaskView.as_view(), name="task_create"),
    path("all", TaskView.as_view(), name="task_get"),
    # path("<int:pk>", TaskView.as_view(), name="task_get"),
    path("update/<int:pk>", TaskView.as_view(), name="task_update"),
]