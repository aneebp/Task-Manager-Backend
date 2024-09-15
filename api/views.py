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
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]  # Enable search functionality
    search_fields = ['title'] 

    def get_queryset(self):
        # Filter tasks to only show tasks created by the currently logged-in user
        queryset = Task.objects.filter(user=self.request.user).order_by('-updated_at')

        #Filter by status (completed or pending)
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=(status.lower() == 'true'))
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#task details
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
