from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from portfolio.views import index, about, contact, work_detail

urlpatterns = [
                  path('', index, name='index'),
                  path('about/', about, name='about'),
                  path('contact/', contact, name='contact'),
                  path('work/<slug:slug>/', work_detail, name='work_detail'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
