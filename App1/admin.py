from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'assigned_to', 'is_completed', 'due_date', 'created_at')
    list_filter = ('is_completed', 'creator', 'assigned_to', 'due_date')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
