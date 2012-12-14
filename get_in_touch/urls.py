from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from get_in_touch import views

urlpatterns = patterns('',
    url(r'^getintouch/$', views.GetInTouchList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
