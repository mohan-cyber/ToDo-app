from django.urls import path
from .views import TodoItemListCreateView, TodoItemRetrieveUpdateDestroyView

urlpatterns = [
    path('todos/', TodoItemListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoItemRetrieveUpdateDestroyView.as_view(), name='todo-item-detail'),
    
]