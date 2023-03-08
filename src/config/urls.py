from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Support API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)


# from django.views.static import serve

urlpatterns = [
    path("exchange-rates/", include("exchange_rates.urls")),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    # path("static/<path:path>/", serve, {"document_root": settings.STATIC_ROOT}),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

_staticfiles_urlpatterns = [path("", include(staticfiles_urlpatterns()))]

if settings.DEBUG:
    urlpatterns += _staticfiles_urlpatterns
