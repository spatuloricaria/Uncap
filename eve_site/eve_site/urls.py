from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

def robots(request):
    return HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")

urlpatterns = patterns('',
    ###########################################################################
    # MISC VIEWS
    (r'^robots\.txt$',                              robots),
    (r'^admin/',                                    include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'eve_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^pages/',                                    include('pages.urls')),
    (r'^accounts/',                                 include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Trick for Django to support static files (security hole: only for Dev environement! remove this on Prod!!!)
        url(r'^media/(?P<path>.*)$',       'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#        url(r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    )
