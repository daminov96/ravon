from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view # new
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



API_TITLE = 'Ravon Taxi Project Docs"'
API_DESCRIPTION = 'Ravon Taxi Project Docs'
yasg_schema_view = get_schema_view(
   openapi.Info(
      title=API_TITLE,
      default_version='v1',
      description=API_DESCRIPTION,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dozolab@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

schema_view = get_swagger_view(title=API_TITLE) # new


admin.site.site_header = "Ravon Taxi administration"
admin.site.site_title = "Ravon Taxi administration"
admin.site.index_title = "Welcome to Ravon Taxi Project"

urlpatterns = [
    path('swagger/', yasg_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('v1/', include('apps.account_account.urls')),
    path('', include('ckeditor_uploader.urls')),
    path('schema/view/', schema_view),
    path('accounts/', include('allauth.urls')),
    path('docs/', include_docs_urls(title='Ravon Taxi', description='A web api of Ravon Taxi models ')),
    # url(r'^', include('rest_framework_tus.urls', namespace='rest_framework_tus')),
    # new

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
