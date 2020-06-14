
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^list$',                  handlers.List.as_view(),            name='inbox_list'),
    url(r'^all$',                   handlers.Inbox.as_view(),           name='inbox_all'),
    url(r'^send-message$',          handlers.SendMessage.as_view(),     name='inbox_send_message'),
    url(r'^contact$',               handlers.Contact.as_view(),         name='inbox_contact'),
]
