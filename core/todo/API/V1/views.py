from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from todo.API.V1.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
