
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^get$',                       handlers.Get.as_view(),                         name='user_get'),
    url(r'^summary$',                   handlers.Summary.as_view(),                     name='user_summary'),
    url(r'^list$',                      handlers.List.as_view(),                        name='user_list'),
    url(r'^create$',                    handlers.Create.as_view(),                      name='user_create'),
    url(r'^delete$',                    handlers.Delete.as_view(),                      name='user_delete'),
    url(r'^sign-in$',                   handlers.SignIn.as_view(),                      name='user_signin'),
    url(r'^sign-up$',                   handlers.SignUp.as_view(),                      name='user_signup'),
    url(r'^edit$',                      handlers.Edit.as_view(),                        name='user_edit'),
    url(r'^active$',                    handlers.Active.as_view(),                      name='user_active'),
    url(r'^inactive$',                  handlers.Inactive.as_view(),                    name='user_inactive'),
    url(r'^change-password$',           handlers.ChangePassword.as_view(),              name='user_change_password'),
    url(r'^reset-password$',            handlers.ResetPasswordRequest.as_view(),        name='user_reset_password'),
    url(r'^reset-password/confirm$',    handlers.ResetPasswordTokenConfirm.as_view(),   name='user_reset_password_confirm'),
    url(r'^reset-password/save$',       handlers.ResetPassword.as_view(),               name='user_reset_password_save'),
]
