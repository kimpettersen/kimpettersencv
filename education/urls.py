from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from education import views


urlpatterns = patterns('',
    url(r'^education/$', views.EducationList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
