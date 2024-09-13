from django.shortcuts import render
from rest_framework import generics,filters
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,TaskSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Task
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


#to list and create task
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]  # Enable search functionality
    search_fields = ['title'] 

    def get_queryset(self):
        queryset = Task.objects.all()
        # Filter by status (completed or pending)
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=(status.lower() == 'true'))
        return queryset

#to delete and update task
class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer