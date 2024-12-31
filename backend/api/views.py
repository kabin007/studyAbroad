from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecentUpdatesSerializer,PriorityTaskSerializer,ApplicationStagesSerializer
from .models import RecentUpdates,PriorityTask,ApplicationStages


# Create your views here.

#api viewset for recent updates
class RecentUpdatesViewSet(viewsets.ModelViewSet):
    queryset=RecentUpdates.objects.all()
    serializer_class=RecentUpdatesSerializer


#api viewset for priority tasks

class PriorityTaskViewSet(viewsets.ModelViewSet):
    queryset=PriorityTask.objects.all()
    serializer_class=PriorityTaskSerializer

class ApplicationStagesViewSet(viewsets.ModelViewSet):
	queryset=ApplicationStages.objects.all()
	serializer_class=ApplicationStagesSerializer



