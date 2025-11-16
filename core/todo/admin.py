from django.contrib import admin
from todo.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "complete", "created_date", "updated_date"]
    list_filter = ["title", "complete"]
    ordering = ["-title"]
    search_fields = ["title"]

admin.site.register(Task, TaskAdmin)
