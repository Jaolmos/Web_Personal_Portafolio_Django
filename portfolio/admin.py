from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):   # Configuracion extendida con campos de solo lectura cread y updated
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)


