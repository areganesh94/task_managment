from django.conf.urls import url, include


from . import views

from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^register/$', views.register, name='register'),
	url(r'^change-password/$', views.change_password, name='change_password'),
	
	url(r'^logout/$', logout, {'template_name': 'account/logout.html'}, name='logout'),

	url(r'^reset-password/$', password_reset, {'template_name': 'account/reset_password.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'account/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'account/reset_password_confirm.html'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'account/reset_password_complete.html'}, name='password_reset_complete'),
]