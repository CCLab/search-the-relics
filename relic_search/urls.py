from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wikilubizabytki.relic_search.views import *

urlpatterns = patterns( '',
    (r'^$', home ),
    (r'^results/$', results ),
    (r'^register/$', register ),
)

urlpatterns += staticfiles_urlpatterns()
