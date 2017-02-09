from django.contrib import admin
from atividades.core.models import *

admin.site.register(Level)
class PriorityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'severity',
    )
admin.site.register(Priority, PriorityAdmin)
class ClusterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'related',
    )
admin.site.register(Cluster)
admin.site.register(Status)
