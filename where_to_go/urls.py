from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from places.views import index, place_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('where_to_go/<int:place_id>/', place_detail, name='place_detail')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
