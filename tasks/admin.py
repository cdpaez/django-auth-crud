from django.contrib import admin
from .models import Task
#metodo para mostrar campos de solo lectura en el panel de administrador de django
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Task, TaskAdmin)