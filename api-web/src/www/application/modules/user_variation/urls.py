
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^get$',                       handlers.Get.as_view(),                         name='user_variation_get'),
    url(r'^list$',                      handlers.List.as_view(),                        name='user_variation_list'),
    # url(r'^create$',                    handlers.Create.as_view(),                      name='user_variation_create'),
    url(r'^edit$',                      handlers.Edit.as_view(),                        name='user_variation_edit'),
    url(r'^delete$',                    handlers.Delete.as_view(),                      name='user_variation_delete'),
    url(r'^update$',                    handlers.Update.as_view(),                      name='user_variation_update'),
    url(r'^get-variation$',             handlers.GetVariation.as_view(),                name='user_variation_get_var'),
]
