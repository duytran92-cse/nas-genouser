
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^statistic$',      handlers.Dashboard.as_view(),     name='dashboard_statistic'),
]
