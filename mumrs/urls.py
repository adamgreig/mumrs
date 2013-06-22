from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers
from movies import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mumrs.views.home', name='home'),
    # url(r'^mumrs/', include('mumrs.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(r'^', include(router.urls))
)
