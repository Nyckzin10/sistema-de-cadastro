from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('pessoas/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]