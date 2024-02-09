from django.contrib import admin
from django.urls import path
from app.views import index, about, project, services, blog, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("about/", about),
    path("project/", project),
    path("services/", services),
    path("blog/", blog),
    path("contact/", contact),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)
