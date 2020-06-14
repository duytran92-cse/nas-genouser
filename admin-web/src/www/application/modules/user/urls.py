
from django.conf.urls import include, url
from . import actions

urlpatterns = [
    url(r'^list$',                                  actions.List.as_view(),     name='user_list'),
    url(r'^create$',                                actions.Create.as_view(),   name='user_create'),
    url(r'^edit/(?P<user_id>([0-9]+))$',            actions.Edit.as_view(),     name='user_update'),
    url(r'^delete/(?P<user_id>([0-9]+))$',          actions.Delete.as_view(),   name='user_delete'),
    url(r'^summary/(?P<user_id>([0-9]+))$',         actions.Summary.as_view(),  name='user_summary'),
    url(r'^active/(?P<user_id>([0-9]+))$',          actions.Active.as_view(),   name='user_active'),
    url(r'^inactive/(?P<user_id>([0-9]+))$',        actions.Inactive.as_view(), name='user_inactive'),
    url(r'^file/(?P<user_id>([0-9]+))$',            actions.File.as_view(),     name='user_file'),
    url(r'^variation/(?P<user_id>([0-9]+))$',       actions.Variation.as_view(),name='user_variation'),
    url(r'^file_remove/(?P<user_id>([0-9]+))$',     actions.FileRemove.as_view(),name='user_file_remove'),
]
