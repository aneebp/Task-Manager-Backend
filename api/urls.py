from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api import views as api_views

urlpatterns = [
    path('register/',api_views.RegisterView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', api_views.TaskListCreateView.as_view(),name='tasks'),
    path('task/<int:pk>/',api_views.TaskDetailsView.as_view(),name='task_detail')

    
]
