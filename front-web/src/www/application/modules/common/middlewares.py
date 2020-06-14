import urllib, urllib2, json, jwt
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from django.conf import settings
from application.modules.user import components

class AuthenticationMiddleware(object):
    def process_request(self, request):
        authorize = False
        if request.get_full_path().startswith('/user'):
            user = components.UserManager().parse_user(request)
            if 'userid' in user:
                authorize = True
            if not authorize:
                return HttpResponseRedirect('/sign-in')