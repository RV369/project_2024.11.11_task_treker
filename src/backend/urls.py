from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tasks/', include('task_treker.urls', namespace='tasks')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
