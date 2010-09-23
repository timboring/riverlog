from django.conf.urls.defaults import *
from django.contrib import admin
from riverlog import views

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
		(r'^river/add$', views.add),
		(r'^river/delete$', views.delete),
		(r'^river/$', views.rivers),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
