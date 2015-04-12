from django.conf.urls import patterns, include, url
from django.contrib import admin
from myApp.views import login_view, logout_view, register_view, get_info, set_info, get_transmit_entries_from, \
    add_new_entry, get_transmit_entries_to


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^apis/login', login_view),
    url(r'^apis/logout', logout_view),
    url(r'^apis/register', register_view),
    url(r'^apis/get$', get_info),
    url(r'^apis/set', set_info),
    url(r'^apis/getentriesfrom', get_transmit_entries_from),
    url(r'^apis/getentriesto', get_transmit_entries_to),
    url(r'apis/addentry', add_new_entry),
)
