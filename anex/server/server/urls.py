from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^nodes/', include('anex.server.leafpile.urls')),
    url(r'^$', 'anex.server.server.views.index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
