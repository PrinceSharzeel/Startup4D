from django.conf.urls import url
from . import views
app_name='rl'
urlpatterns = [
	url(r'^sky',views.sky),

	url(r'^serch', views.serch),

	url(r'^unlog_serch', views.unlog_serch),

	url(r'^signup_contrib', views.signup_contrib),
	url(r'^login_contrib',views.login_contrib),

	url(r'^leave', views.leave),

	url(r'^adm', views.adm),

	url(r'^logout', views.logt),
	url(r'^verif/(?P<prodname>[\w|\W]+)/$', views.verif, name='verif'),

	url(r'^rem/(?P<prodname>[\w|\W]+)/$', views.rem, name='rem'),

]
