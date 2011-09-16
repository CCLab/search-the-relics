from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wiki_zabytki.relic_search.views import *

urlpatterns = patterns( '',
    (r'^$', home ),
    (r'^results/$', results ),
)

urlpatterns += staticfiles_urlpatterns()
