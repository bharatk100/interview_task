from django.urls import path
from .views import ProjectView

urlpatterns = [
    path("create", ProjectView.as_view(), name="project_create"),
    path("<int:pk>", ProjectView.as_view(), name="project_get"),
    path("update/<int:pk>", ProjectView.as_view(), name="project_update"),
    path("delete/<int:pk>", ProjectView.as_view(), name="project_delete"),
]