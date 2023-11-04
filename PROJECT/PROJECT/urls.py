from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from mainApp.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Ikki buyuk alloma API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tursunovotabekkuva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('topics/', TopicsAPIView.as_view()),
    path('audios/', AudiosAPIView.as_view()),
    path('audios/<int:pk>/', AudiosByTopicAPIView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

