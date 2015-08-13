#__*__ coding:utf-8 __*__
from django.conf.urls import *
from django.contrib import admin
from webapp.views import curr_datetime, index, add
from booksapp.models import Publisher
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', curr_datetime),
    url(r'^$', 'webapp.views.index', name='home'),
    url(r'^add/$', 'webapp.views.add', name='add'),
    url(r'getdir/$', 'calcmd5_app.views.GetDir', name='GetDir'),
    url(r'calcmd5/$', 'calcmd5_app.views.CalcMd5', name='CalcMd5'),
    url(r'getmd5/$', 'Calcmd5App.views.GetMd5', name='GetMd5'),
)
urlpatterns += patterns('',
    url(r'^search/$', 'booksapp.views.search'),
)