from django.contrib import admin

from .models import AppointedPerformer, CompletedTask, Task, VerifiedTask


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
