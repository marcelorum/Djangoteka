from django.contrib import admin
from .models import Task

# Método ara agregar fields al panel
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Entrada en el panel de Admin 
admin.site.register(Task, TaskAdmin)