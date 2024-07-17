from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from portfolio.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
