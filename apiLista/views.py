from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class TaskViews(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.request.user.task_set.all()