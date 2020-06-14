from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from notasquare.urad_api import *
from application.models import *
from application import constants
from django.contrib.auth.hashers import make_password
import uuid
from . import components


class List(handlers.standard.ListHandler):
    def create_query(self, data):
        query = User.objects
        if data.get('username', '') != '' :
            query = query.filter(name__contains=data['username'])
        return query
    def serialize_entry(self, user):
        return {
            'id':               user.id,
            'username':         user.username,
            'email':            user.email,
            'fullname':         user.userprofile.fullname,
        }



class Get(handlers.standard.GetHandler):
    def get_data(self, data):
        user = None
        try:
            if 'username' in data and data['username']:
                user = User.objects.get(username=data['username'])
            if 'email' in data and data['email']:
                user = User.objects.get(email=data['email'])
            if 'id' in data and data['id']:
                user = User.objects.get(pk=data['id'])
        except User.DoesNotExist:
            return None
        else:
            return {
                'id':           user.id,
                'username':     user.username,
                'fullname' :    user.userprofile.fullname,
                'email':        user.email,
                'joined_at':    user.joined_at,
                'is_active':    user.is_active,
                'photo':        user.userprofile.photo,
                'science_filter': user.userprofile.science_filter,
                'private_result': components.ExtraUserHelper().get_private_result(user.id)
            }



class SignIn(handlers.standard.FormHandler):
    def post_data(self, data):
        try:
            user = User.objects.get(Q(email=data['text']) | Q(username=data['text']))
            if check_password(data['password'], user.password):

                self.set_response_data({
                    'id':           user.id,
                    'username':     user.username,
                    'fullname' :    user.userprofile.fullname,
                    'email':        user.email,
                    'joined_at':    user.joined_at,
                    'is_active':    user.is_active,
                    'photo':        user.userprofile.photo,
                    'science_filter': user.userprofile.science_filter,
                    'private_result': components.ExtraUserHelper().get_private_result(user.id)
                })
        except User.DoesNotExist:
            return None
        return None



class SignUp(handlers.standard.FormHandler):
    def post_data(self, data):
        salt = uuid.uuid4()
        bcrupted_pass = make_password(data['password'], salt=str(salt))
        user = User(username=data['username'], email=data['email'], password=bcrupted_pass, salt=str(salt))
        user.save()
        user_profile = UserProfile(
            user=user,
            position=       user.id
        )
        user_profile.save()
        self.set_response_data({
            'id':           user.id,
            'username':     user.username,
            'fullname' :    user.userprofile.fullname,
            'email':        user.email,
            'joined_at':    user.joined_at,
            'is_active':    user.is_active,
            'photo':        user.userprofile.photo,
            'science_filter': user.userprofile.science_filter,
            'private_result': components.ExtraUserHelper().get_private_result(user.id)
        })

class Summary(handlers.standard.GetHandler):
    def get_data(self, data):
        user = User.objects.get(pk=data['id'])
        achievements = [x.__dict__ for a in user.userachievement_set.all()]
        friends = []
        for f in user.friend.all():
            friends.append({
                'username': f.user.username,
                'photo': f.user.userprofile.photo,
                'num_of_new_messages': UserMessage.objects.filter(sender_id=f.user.id, receiver_id=user.id, is_read=False).count(),
            })
        # Get User Variation
        upload = UserUpload.objects.filter(user_id=data['id'], is_disable=False)
        user_variation = ''
        if upload:
            user_variation = 'active'
        return {
            'id':                       user.id,
            'username':                 user.username,
            'email':                    user.email,
            'joined_at':                user.joined_at.strftime('%m/%d/%Y'),
            'achievements':             achievements,
            'is_active_code':           user.is_active,
            'is_active':                helpers.translate_constant_select(user.is_active, constants.ACTIVE_STATUS),
            'fullname':                 user.userprofile.fullname,
            'position':                 user.userprofile.position,
            'rank':                     user.userprofile.rank,
            'about':                    user.userprofile.about,
            'photo':                    user.userprofile.photo,
            'genetic_type_code':        user.userprofile.genetic_type,
            'genetic_type':             helpers.translate_constant_select(user.userprofile.genetic_type, constants.GENETIC_TYPE),
            'gender':                   helpers.translate_constant_select(user.userprofile.gender, constants.GENDER),
            'country':                  helpers.translate_constant_select(user.userprofile.country, constants.COUNTRIES),
            'education':                helpers.translate_constant_select(user.userprofile.education, constants.EDUCATION),
            'work':                     user.userprofile.work,
            'birthday':                 user.userprofile.birthday,
            'account_paypal':           user.userprofile.account_paypal,
            'friends':                  friends,
            'private_result':           components.ExtraUserHelper().get_private_result(user.id),
            'user_variation':           user_variation,
            'science_filter':           user.userprofile.science_filter
        }



class Create(handlers.standard.CreateHandler):
    def create(self, data):
        salt = uuid.uuid4()
        bcrupted_pass = make_password(data['password'], salt=str(salt))
        user = User(username=data['username'], email=data['email'], password=bcrupted_pass, salt=str(salt))
        user.save()
        user_profile = UserProfile(
            user=user,
            position=       user.id
        )
        user_profile.save()
        return user



class Edit(handlers.standard.UpdateHandler):
    def update(self, data):
        user = User.objects.get(pk=data['user_id'])
        if data.get('username', ''):
            user.username = data.get('username')
        if data.get('email', ''):
            user.email = data.get('email')
        if data.get('is_active', ''):
            user.is_active = data.get('is_active')
        user.save()

        userprofile = UserProfile.objects.get(user_id=data['user_id'])
        if data.get('fullname', '') != '' :
            userprofile.fullname = data['fullname'].strip()
        if data.get('position', '') != '' :
            userprofile.position = data['position'].strip()
        if data.get('about', '') != '' :
            userprofile.about = data['about'].strip()
        if data.get('birthday', '') != '' :
            userprofile.birthday = data['birthday'].strip()
        if data.get('gender', '') != '' :
            userprofile.gender = data['gender'].strip()
        if data.get('country', '') != '' :
            userprofile.country = data['country']
        if data.get('education', '') != '' :
            userprofile.education = data['education']
        if data.get('work', '') != '' :
            userprofile.work = data['work'].strip()
        if data.get('photo', '') != '' :
            userprofile.photo = data['photo'].strip()
        if data.get('rank', '') != '' :
            userprofile.rank = data['rank'].strip()
        if data.get('account_paypal', '') != '' :
            userprofile.account_paypal = data['account_paypal'].strip()
        if data.get('genetic_type_code', '') != '' :
            if data['genetic_type_code'] != userprofile.genetic_type:
                # Add notification
                user_noti = UserNotification()
                user_noti.user_id = data['user_id']
                user_noti.kind = 'rank'
                user_noti.message = 'New rank assigned'
                user_noti.save()
            userprofile.genetic_type = data['genetic_type_code'].strip()
        if data.get('science_filter', ''):
            userprofile.science_filter = data.get('science_filter')
        userprofile.save()
        return user


class Active(handlers.standard.UpdateHandler):
    def update(self, data):
        try:
            user = User.objects.get(pk=data['user_id'])
            user.is_active = True
            user.save()
            return user
        except User.DoesNotExist:
            return None


class Inactive(handlers.standard.UpdateHandler):
    def update(self, data):
        try:
            user = User.objects.get(pk=data['user_id'])
            user.is_active = False
            user.save()
            return user
        except User.DoesNotExist:
            return None


class ChangePassword(handlers.standard.UpdateHandler):
    def update(self, data):
        salt = uuid.uuid4()
        bcrupted_pass = make_password(data['new_password'], salt=str(salt))
        user = User.objects.get(pk=data['id'])
        user.password = bcrupted_pass
        user.salt = salt
        user.save()
        return user


class ResetPasswordRequest(handlers.standard.FormHandler):
    def post_data(self, data):
        try:
            user = User.objects.get(email=data['email'])

            rand_str = str(uuid.uuid4()).replace('-','')
            token = Signer().sign(rand_str)
            user_token = UserResetPassToken(user_id=user.id, token=token)
            user_token.save()

            self.set_response_data({
                'token':        user_token.token,
                'user_id':      user.id,
                'email':        user.email,
                'username':     user.username,
            })
        except User.DoesNotExist:
            return None



class ResetPasswordTokenConfirm(handlers.standard.GetHandler):
    def get_data(self, data):
        try:
            user_token = UserResetPassToken.objects.get(user_id=data['user_id'], token=data['token'])
            return True
        except UserResetPassToken.DoesNotExist:
            return False



class ResetPassword(handlers.standard.FormHandler):
    def post_data(self, data):
        salt = uuid.uuid4()
        bcrupted_pass = make_password(data['new_password'], salt=str(salt))
        user = User.objects.get(pk=data['id'])
        user.password = bcrupted_pass
        user.salt = salt
        user.save()
        try:
            UserResetPassToken.objects.get(token=data['token']).delete()
        except UserResetPassToken.DoesNotExist:
            pass
        self.set_response_data({
            'id':           user.id,
            'username':     user.username,
            'fullname' :    user.userprofile.fullname,
            'email':        user.email,
            'joined_at':    user.joined_at,
            'is_active':    user.is_active,
            'photo':        user.userprofile.photo,
        })



class Delete(handlers.standard.DeleteHandler):
    def delete(self, data):
        user = User.objects.get(pk=data['user_id'])
        user.delete()
        return 1
