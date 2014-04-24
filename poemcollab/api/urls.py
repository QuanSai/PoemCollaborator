from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PoemList, PoemDetail


urlpatterns = patterns('api.views',
    url(r'^poem-list/$', PoemList.as_view()),
    url(r'^poem/(?P<pk>[0-9]+)$', PoemDetail.as_view()),
)


urlpatterns = format_suffix_patterns(urlpatterns)
