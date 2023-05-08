from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


app_patterns = [
    path('', include('CoreApp.urls')),
]

urlpatterns = [
    # re_path(r'^auth/', include('djoser.urls.jwt')),
    # re_path(r'^auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(app_patterns)),
]


from decouple import config
IS_DEV = config('IS_DEV')

if IS_DEV:
    
    from rest_framework.schemas import get_schema_view

    schema_view = get_schema_view(
        title="API Schema", description="Guide for the REST API")

    swagger_view = TemplateView.as_view(
        template_name="Swagger.html", extra_context={"schema_url": "api-schema"}
    )
    
    urlpatterns += [
        path('api-schema/', schema_view, name='api-schema'),
        path('', swagger_view, name='swagger-ui'),
        path('__debug__/', include('debug_toolbar.urls')),
    ]


