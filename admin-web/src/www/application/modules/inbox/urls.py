
from django.conf.urls import include, url
from . import actions

urlpatterns = [
    url(r'^list$',                                  actions.List.as_view(),     name='user_list'),
    url(r'^messages/(?P<inbox_id>([0-9]+))$',       actions.Detail.as_view(),   name='user_detail')
]

