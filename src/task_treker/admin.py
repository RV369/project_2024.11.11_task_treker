from django.contrib import admin

from .models import Task, AppointedPerformer, VerifiedTask, CompletedTask


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description', 
        'create_date', 
        'author_task',
        )

admin.site.register(Task, TaskAdmin)
admin.site.register(AppointedPerformer)
admin.site.register(VerifiedTask)
admin.site.register(CompletedTask)
