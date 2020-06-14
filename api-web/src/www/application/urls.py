from django.conf.urls import include, url

urlpatterns = [
    url(r'^user/',                           include('application.modules.user.urls')),
    url(r'^inbox/',                          include('application.modules.inbox.urls')),
    url(r'^dashboard/',                      include('application.modules.dashboard.urls')),
    url(r'^user-variation/',                 include('application.modules.user_variation.urls')),
    url(r'^user-upload/',                    include('application.modules.user_upload.urls')),
]
