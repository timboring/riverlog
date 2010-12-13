from django.conf.urls.defaults import *
from django.contrib import admin
from riverlog import views
import settings

admin.autodiscover()

urlpatterns = patterns('',
		(r'^river/add$', views.add),
		(r'^river/delete$', views.delete),
		(r'^river/$', views.rivers),
		('^$', views.home),
)

# urls for serving static content/media using django's dev server
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
	)
