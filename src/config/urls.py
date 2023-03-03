from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

# from django.views.static import serve

urlpatterns = [
    path("exchange-rates/", include("exchange_rates.urls")),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    # path("static/<path:path>/", serve, {"document_root": settings.STATIC_ROOT})
]

_staticfiles_urlpatterns = [path("", include(staticfiles_urlpatterns()))]

if settings.DEBUG:
    urlpatterns += _staticfiles_urlpatterns
