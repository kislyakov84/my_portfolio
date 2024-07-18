from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from portfolio.views import index, about, contact, work_detail


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('work/<slug:slug>/', work_detail, name='work_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
