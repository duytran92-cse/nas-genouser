from django.conf.urls import include, url
from application.modules.user import actions as user_actions
urlpatterns = [
    url(r'^',                           include('application.modules.home.urls')),
    url(r'^user/',                      include('application.modules.user.urls')),
    url(r'^sign-in$',                   user_actions.SignIn.as_view(),                  name='user_signin'),
    url(r'^sign-up$',                   user_actions.SignUp.as_view(),                  name='user_signup'),
    url(r'^sign-out$',                  user_actions.SignOut.as_view(),                 name='user_signout'),
    url(r'^reset-password$',            user_actions.ResetPasswordRequest.as_view(),    name='user_reset_password'),
    url(r'^reset-password/confirm$',    user_actions.ResetPassword.as_view(),           name='user_reset_password_confirm'),
    url(r'^reset-password/save$',       user_actions.ResetPassword.as_view(),           name='user_reset_password_save'),
    url(r'^reset-password/sent$',       user_actions.ResetPasswordRequestSent.as_view(),           name='user_reset_password_sent'),
]

