from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('riverlog.views',
		(r'^river/add$', 'add'),
		(r'^river/delete$', 'delete'),
		(r'^river/importruns$', 'importruns'),
		(r'^river/(\d+)/$', 'river'),
		(r'^river/$', 'rivers'),
		('^$', 'rivers'),
)

# urls for serving static content/media using django's dev server
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
	)
