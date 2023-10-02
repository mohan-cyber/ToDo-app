from django.contrib import admin

#models

from .models import TodoItem


admin.site.register(TodoItem)
