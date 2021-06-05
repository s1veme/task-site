from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),

    path('api/user/', include('authentication.urls')),
    path('api/infomrmation/', include('leaderboard.urls'))

]
