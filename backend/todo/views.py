from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

#import models
from .models import TodoItem

#import serializer
from .serializers import TodoItemSerializer

class TodoItemListCreateView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    # permission_classes = [IsAuthenticated]

class TodoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    # permission_classes = [IsAuthenticated]

