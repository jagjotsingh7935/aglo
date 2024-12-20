from django.contrib import admin
from .models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'due_date', 'timestamp']
    list_filter = ['status', 'due_date']
    search_fields = ['title', 'description']
    readonly_fields = ['timestamp']
