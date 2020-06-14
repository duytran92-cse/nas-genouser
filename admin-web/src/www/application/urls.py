from django.conf.urls import include, url

urlpatterns = [
    url(r'^',                                   include('application.modules.dashboard.urls')),
    url(r'^dashboard$',                         include('application.modules.dashboard.urls')),
    url(r'^user/',                              include('application.modules.user.urls')),
    url(r'^inbox/',                              include('application.modules.inbox.urls')),
]
