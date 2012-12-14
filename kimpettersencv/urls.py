from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
    ('^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^', include('get_in_touch.urls')),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
)
