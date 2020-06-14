
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^get$',                       handlers.Get.as_view(),                         name='user_upload_get'),
    # url(r'^list$',                      handlers.List.as_view(),                        name='user_variation_list'),
    url(r'^check_upload$',              handlers.CheckUpload.as_view(),                 name='user_variation_check_upload'),
    url(r'^edit$',                      handlers.Edit.as_view(),                        name='user_upload_edit'),
    url(r'^delete$',                    handlers.Delete.as_view(),                      name='user_variation_delete'),
]
