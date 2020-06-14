from django.conf import settings
import jwt
from django.http import HttpResponse, HttpResponseRedirect

class UserStore(object):
    def __init__(self, container):
        self.container = container
    def sign_in(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/sign-in', POST=data)
    def sign_up(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/sign-up', POST=data)
    def profile(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user/summary', GET={'id': id})
    def get(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/get', GET=data)
    def edit_profile(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/edit', POST=data)
    def edit_avatar(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/edit', POST=data)
    def change_password(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/change-password', POST=data)
    def reset_password_request(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/reset-password', POST=data)
    def reset_password_save(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/reset-password/save', POST=data)
    def check_reset_pass_token(self, user_id, token):
        return self.container.call_api(settings.USER_API_URL + '/user/reset-password/confirm', GET={'user_id': user_id, 'token': token})
    def get_inbox(self, data):
        return self.container.call_api(settings.USER_API_URL + '/inbox/all', GET=data)
    def get_contact(self, data):
        return self.container.call_api(settings.USER_API_URL + '/inbox/contact', GET=data)
    def send_message(self, data):
        return self.container.call_api(settings.USER_API_URL + '/inbox/send-message', POST=data)
    def update_variation(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user-variation/edit', POST=data)
    def user_upload(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user-upload/edit', POST=data)

class UserManager(object):
    def __init__(self):
        pass
    def parse_user(self,request):
        encoded = request.COOKIES.get('_gpfront_jwt')
        if encoded:
            user = jwt.decode(encoded, settings.OAUTH_CLIENT_EK, algorithms=['HS256'])
            if 'userid' in user:
                return user
        return False
    def refresh_user_cookie(self,user,request,redirect):
        data = {
            'userid'    : user['id'],
            'username'  : user['username'],
            'email'     : user['email'],
            'fullname'  : user['fullname'],
            'photo'     : user['photo'],
            'science_filter': user['science_filter'],
            'private_result': user['private_result']
        }
        domain = '.'+'.'.join(request.META['HTTP_HOST'].split('.')[-2:])
        encoded = jwt.encode(data, settings.OAUTH_CLIENT_EK, algorithm='HS256')
        response =  HttpResponseRedirect(redirect)
        response.set_cookie('_gpfront_jwt',encoded,max_age=settings.OAUTH_EXPIRE_TIME,path='/',domain=domain)
        return response
