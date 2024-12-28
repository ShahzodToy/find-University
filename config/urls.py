from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="University API",
      default_version='v1',
      description="Univercity description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abdashevshahzod340gmail.com"),
      license=openapi.License(name="Mine license"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('set_languages/', include('django.conf.urls.i18n')),
)

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]