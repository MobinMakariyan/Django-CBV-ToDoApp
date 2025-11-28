from django.urls import path
from rest_framework.routers import DefaultRouter
from todo.API.V1.views import TaskViewSet

app_name = "todo-api-v1"

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="Tasks")
urlpatterns = router.urls
