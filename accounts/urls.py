from django.conf.urls import include, url, patterns
from views import register, login, profile, logout

urlpatterns = patterns('',
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
)