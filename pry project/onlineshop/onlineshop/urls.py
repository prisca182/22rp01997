from django.contrib import admin
from django.urls import include, path  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # Includes the store app's URLs
]