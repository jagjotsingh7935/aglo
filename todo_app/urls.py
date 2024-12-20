from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoItemViewSet, index

router = DefaultRouter()
router.register(r'todos', ToDoItemViewSet, basename='todo')

urlpatterns = [
    path('', index, name='index'),  # Route for the index.html file
    path('api/', include(router.urls)),  # API routes
]
