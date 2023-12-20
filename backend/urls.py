from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('eccomerce.urls')),  # Replace 'your_app_name' with the actual name of your app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
