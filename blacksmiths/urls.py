# encoding: utf-8
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from content.views import BaseView, BookView, SuccessView, CategoryView

urlpatterns = [
    url(r'^$', BaseView.as_view(), name='home'),
    url(r'^catalog/(?P<slug>[-\w]+)-(?P<pk>\d+)$', CategoryView.as_view(), name='category'),
    url(r'^book$', BookView.as_view(), name='book'),
    url(r'^success', SuccessView.as_view(), name='success'),
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
