from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('cssa_web.views',
    url(r'^cssa/$', 'index'),
    url(r'^cssa/register/$', 'register'),
    url(r'^cssa/confirm/(?P<username>\w+)&(?P<random_num>\d+)$', 'confirm'),
    url(r'^cssa/login/$', 'login'),
    url(r'^cssa/success/email_sent/$', 'email_sent'),
    url(r'^cssa/event/$', 'event'),
    url(r'^cssa/event/addEvent', 'addEvent'),
    url(r'^cssa/resource/$', 'resource'),
    url(r'^cssa/resource/addResource', 'addResource')
#    url(r'^cssa/resource/$', 'resource'),
##    url(r'^cssa/photos/$', 'photo'),
)

#urlpatterns += patterns('poll.views',
#    url(r'^poll/$', 'index'),
#    url(r'^poll/(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^poll/(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^poll/(?P<poll_id>\d+)/vote/$', 'vote'),
#)

#urlpatterns += patterns('try2.views',
#    (r'^about/', AboutView.as_view()),
#)