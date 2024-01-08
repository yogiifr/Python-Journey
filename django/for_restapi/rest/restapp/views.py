from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-date_create')
    serializers_class = TaskSerializers