from django.conf.urls.defaults import patterns, include, url

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^$', 'index', name='index'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
