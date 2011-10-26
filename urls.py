from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'audio.views.listfile', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
