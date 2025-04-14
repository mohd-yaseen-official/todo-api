from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'is_deleted', 'created_at')

admin.site.register(Task, TaskAdmin)