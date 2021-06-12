from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),

    path('api/user/', include('user.urls')),
    path('api/infomrmation/', include('leaderboard.urls')),
    path('api/tasks/', include('tasks.urls'))

]
