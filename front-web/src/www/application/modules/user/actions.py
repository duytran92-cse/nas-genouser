from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import loader, Context
from django.contrib import messages

from notasquare.urad_web import actions, widgets, renderers
from application.themes.genopedia import renderers as genopedia_renderers
from application.modules.common import page_contexts, actions as common_actions, components as common_components, helper
from application import constants
from application.themes.genopedia import renderers as genopedia_renderers
from application.themes.genopedia import widgets as genopedia_widgets
from . import components

import json
import re,jwt



class SignIn(common_actions.BaseAction):
    class SignInWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class SignInWidgetRenderer(renderers.BaseRenderer):
        def __init__(self,request):
            self.request = request
        def render(self, sign_in_widget):

            template = loader.get_template('genopedia/home/sign_in.html')
            context = {}
            context['current_url'] = 'http' + ('', 's')[self.request.is_secure()] + '://'+ self.request.META['HTTP_HOST']+ self.request.META['REQUEST_URI']
            context['messages'] = sign_in_widget.messages
            context['form_data'] = sign_in_widget.form_data
            return template.render(context)
    def create_sign_in_widget(self):
        sign_in_widget = self.SignInWidget()
        sign_in_widget.renderer = self.SignInWidgetRenderer(self.request)
        sign_in_widget.form_data = {}
        return sign_in_widget
    def GET(self):
        page_context = self.create_page_context()
        sign_in_widget = self.create_sign_in_widget()
        sign_in_widget.messages = messages.get_messages(self.request)
        page_context.add_widget(sign_in_widget)
        response = HttpResponse(page_context.render())
        domain = '.'+'.'.join(self.request.META['HTTP_HOST'].split('.')[-2:])
        if self.request.GET.get('redirect'):
            response.set_cookie('redirect',self.request.GET.get('redirect'),max_age=3600,path='/',domain=domain)
        else:
            response.delete_cookie('redirect',path='/',domain=domain)
        return response


    def POST(self):
        if not self.params['text']:
            messages.error(self.request, "Username or email is required", extra_tags='text')
        if not self.params['password']:
            messages.error(self.request, "Password is required", extra_tags='password')
        if (self.params['text']) and (self.params['password']):
            user = components.UserStore(self.get_container()).sign_in({'text': self.params['text'], 'password': self.params['password']})['data']
            if user:
                redirect = self.request.COOKIES.get('redirect')
                if not redirect:
                    redirect = '/user/profile'
                return components.UserManager().refresh_user_cookie(user,self.request,redirect)
            else:
                messages.error(self.request, 'Username or password is incorrect', extra_tags='password')
        page_context = self.create_page_context()
        sign_in_widget = self.create_sign_in_widget()
        sign_in_widget.messages = messages.get_messages(self.request)
        sign_in_widget.form_data = self.params
        page_context.add_widget(sign_in_widget)
        return HttpResponse(page_context.render())



class SignUp(common_actions.BaseAction):
    class SignUpWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class SignUpWidgetRenderer(renderers.BaseRenderer):
        def render(self, sign_up_widget):
            template = loader.get_template('genopedia/home/sign_up.html')
            context = {}
            context['messages'] = sign_up_widget.messages
            context['form_data'] = sign_up_widget.form_data
            return template.render(context)
    def create_sign_up_widget(self):
        sign_up_widget = self.SignUpWidget()
        sign_up_widget.renderer = self.SignUpWidgetRenderer()
        sign_up_widget.form_data = {}
        return sign_up_widget
    def GET(self):
        page_context = self.create_page_context()
        sign_up_widget = self.create_sign_up_widget()
        sign_up_widget.messages = messages.get_messages(self.request)
        page_context.add_widget(sign_up_widget)
        response = HttpResponse(page_context.render())
        domain   = '.'+'.'.join(self.request.META['HTTP_HOST'].split('.')[-2:])
        if self.request.GET.get('redirect'):
            response.set_cookie('redirect',self.request.GET.get('redirect'),max_age=3600,path='/',domain=domain)

        return response
    def POST(self):
        if not self.params['username']:
            messages.error(self.request, "Username is required", extra_tags='username')
        if not self.params['email']:
            messages.error(self.request, "Email is required", extra_tags='email')
        if self.params['email'] and not re.match("[^@]+@[^@]+\.[^@]+", self.params['email']):
            messages.error(self.request, "Invalid email address", extra_tags='email')
        if not self.params['password']:
            messages.error(self.request, "Password is required", extra_tags='password')
        if not self.params['confirm']:
            messages.error(self.request, "Comfirm password is required", extra_tags='confirm')
        if self.params['password'] and self.params['confirm']:
            if self.params['confirm'].strip() != self.params['password'].strip():
                messages.error(self.request, "Confirm password is not match to password", extra_tags='confirm')
            if re.match('^[A-Za-z0-9_]+$', self.params['username']) is None:
                messages.error(self.request, "Letter, digit, and underscore only, please try again", extra_tags='password')
            if len(self.params['password']) < 2:
                messages.error(self.request, "Password must be at least 2 characters", extra_tags='password')
        if self.params['username'] and self.params['email'] and self.params['confirm'].strip() == self.params['password'].strip() and re.match("[^@]+@[^@]+\.[^@]+", self.params['email']):
            existed_username =  components.UserStore(self.get_container()).get({'username': self.params['username']})['data']['record']
            existed_email =     components.UserStore(self.get_container()).get({'email':    self.params['email']})['data']['record']
            if existed_username != None:
                messages.error(self.request, "Username is already taken, please try another", extra_tags='username')
            if existed_email != None:
                messages.error(self.request, "Email is already taken, please try another", extra_tags='email')
            if existed_email == None and existed_username == None:
                user = components.UserStore(self.get_container()).sign_up(self.params)['data']
                if user:
                    redirect = self.request.COOKIES.get('redirect')
                    if not redirect:
                        redirect = '/user/profile'
                    return components.UserManager().refresh_user_cookie(user,self.request,redirect)

        page_context = self.create_page_context()
        sign_up_widget = self.create_sign_up_widget()
        sign_up_widget.messages = messages.get_messages(self.request)
        sign_up_widget.form_data = self.params
        page_context.add_widget(sign_up_widget)
        return HttpResponse(page_context.render())


class SignOut(common_actions.BaseAction):
    def GET(self):
        domain = '.'+'.'.join(self.request.META['HTTP_HOST'].split('.')[-2:])
        if self.request.GET.get('redirect'):
            response = HttpResponseRedirect(self.request.GET.get('redirect'))
        else:
            response = HttpResponseRedirect('/')
        response.delete_cookie('_gpfront_jwt',path='/',domain=domain)
        response.delete_cookie('redirect',path='/',domain=domain)
        return response



class Profile(common_actions.BaseAction):
    class ProfileWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class ProfileWidgetRenderer(renderers.BaseRenderer):
        def render(self, profile_widget):
            template = loader.get_template('genopedia/home/profile.html')
            context = {}
            context['user'] = profile_widget.user
            return template.render(context)
    def create_profile_widget(self):
        profile_widget = self.ProfileWidget()
        profile_widget.renderer = self.ProfileWidgetRenderer()
        user = components.UserManager().parse_user(self.request)
        profile_widget.user = components.UserStore(self.get_container()).profile(user['userid'])['data']['record']
        return profile_widget
    def GET(self):
        page_context = self.create_page_context()
        profile_widget = self.create_profile_widget()
        page_context.add_widget(profile_widget)
        return HttpResponse(page_context.render())


class EditProfile(common_actions.BaseAction):
    class EditProfiletWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class EditProfiletWidgetRenderer(renderers.BaseRenderer):
        def render(self, edit_profile_widget):
            template = loader.get_template('genopedia/home/edit_profile.html')
            context = {}
            context['user'] = edit_profile_widget.user
            context['gender'] = edit_profile_widget.gender
            context['countries'] = edit_profile_widget.countries
            context['education'] = edit_profile_widget.education
            return template.render(context)
    def create_edit_profile_widget(self):
        edit_profile_widget = self.EditProfiletWidget()
        edit_profile_widget.renderer = self.EditProfiletWidgetRenderer()
        user = components.UserManager().parse_user(self.request)
        edit_profile_widget.user = components.UserStore(self.get_container()).profile(user['userid'])['data']['record']
        edit_profile_widget.gender = constants.GENDER
        edit_profile_widget.countries = constants.COUNTRIES
        edit_profile_widget.education = constants.EDUCATION
        return edit_profile_widget
    def GET(self):
        page_context = self.create_page_context()
        edit_profile_widget = self.create_edit_profile_widget()
        page_context.add_widget(edit_profile_widget)
        return HttpResponse(page_context.render())
    def POST(self):
        if self.request.FILES.get('photo', None) != None:
            photo = helper.Helper().uploader(self.request.FILES['photo'])
            if photo:
                self.params['photo'] = photo
        user = components.UserManager().parse_user(self.request)
        self.params['user_id'] = user['userid']
        components.UserStore(self.get_container()).edit_profile(self.params)
        user = components.UserStore(self.get_container()).profile(user['userid'])['data']['record']
        if user:
            return components.UserManager().refresh_user_cookie(user,self.request,'/user/profile')
        else:
            return HttpResponseRedirect('/user/profile/edit')



class EditAvatar(common_actions.BaseAction):
    class EditAvatarWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class EditAvatarWidgetRenderer(renderers.BaseRenderer):
        def render(self, edit_avatar_widget):
            template = loader.get_template('genopedia/home/edit_avatar.html')
            context = {}
            context['user'] = edit_avatar_widget.user
            return template.render(context)
    def create_edit_avatar_widget(self):
        edit_avatar_widget = self.EditAvatarWidget()
        edit_avatar_widget.renderer = self.EditAvatarWidgetRenderer()
        user = components.UserManager().parse_user(self.request)
        edit_avatar_widget.user = components.UserStore(self.get_container()).profile(user['userid'])['data']['record']
        edit_avatar_widget.gender = constants.GENDER
        edit_avatar_widget.countries = constants.COUNTRIES
        edit_avatar_widget.education = constants.EDUCATION
        return edit_avatar_widget
    def GET(self):
        page_context = self.create_page_context()
        edit_avatar_widget = self.create_edit_avatar_widget()
        page_context.add_widget(edit_avatar_widget)
        return HttpResponse(page_context.render())
    def POST(self):
        if self.request.FILES.get('photo', None) != None:
            photo = helper.Helper().uploader(self.request.FILES['photo'])
            if photo:
                self.params['photo'] = photo
        user = components.UserManager().parse_user(self.request)
        self.params['user_id'] = user['userid']
        components.UserStore(self.get_container()).edit_avatar(self.params)['data']
        user = components.UserStore(self.get_container()).profile(user['userid'])['data']['record']
        if user:
            # update avatar in user cookie
            return components.UserManager().refresh_user_cookie(user,self.request,'/user/profile')
        else:
            return HttpResponseRedirect('/user/profile/edit')


class ChangePassword(common_actions.BaseAction):
    class ChangePasswordtWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class ChangePasswordtWidgetRenderer(renderers.BaseRenderer):
        def render(self, change_password_widget):
            template = loader.get_template('genopedia/home/change_password.html')
            context = {}
            context['messages'] = change_password_widget.messages
            return template.render(context)
    def create_change_password_widget(self):
        change_password_widget = self.ChangePasswordtWidget()
        change_password_widget.renderer = self.ChangePasswordtWidgetRenderer()
        return change_password_widget
    def GET(self):
        page_context = self.create_page_context()
        change_password_widget = self.create_change_password_widget()
        change_password_widget.messages = messages.get_messages(self.request)
        page_context.add_widget(change_password_widget)
        return HttpResponse(page_context.render())
    def POST(self):
        if not self.params['new_password']:
            messages.error(self.request, "Password is required", extra_tags='new_password')
        if not self.params['confirm_password']:
            messages.error(self.request, "Confirm password is required", extra_tags='confirm_password')
        if self.params['new_password'] and self.params['confirm_password']:
            if len(self.params['new_password']) < 2:
                messages.error(self.request, "Password must be at least 2 characters", extra_tags='new_password')
            if self.params['confirm_password'].strip() != self.params['new_password'].strip():
                messages.error(self.request, "Confirm password is not match to password", extra_tags='confirm_password')
            else:
                user = components.UserManager().parse_user(self.request)
                self.params['id'] = user['userid']
                user = components.UserStore(self.get_container()).change_password(self.params)
                if user:
                    return HttpResponseRedirect('/user/profile')
                else:
                    messages.error(self.request, "Opps!, something went wrong, please try again")
        return HttpResponseRedirect('/user/change-password')



class ResetPasswordRequest(common_actions.BaseAction):
    class ResetPasswordRequesttWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class ResetPasswordRequesttWidgetRenderer(renderers.BaseRenderer):
        def render(self, reset_password_request_widget):
            template = loader.get_template('genopedia/home/reset_password_request.html')
            context = {}
            context['messages'] = reset_password_request_widget.messages
            context['form_data'] = reset_password_request_widget.form_data
            return template.render(context)
    def create_reset_password_request_widget(self):
        reset_password_request_widget = self.ResetPasswordRequesttWidget()
        reset_password_request_widget.renderer = self.ResetPasswordRequesttWidgetRenderer()
        reset_password_request_widget.form_data = {}
        return reset_password_request_widget
    def GET(self):
        page_context = self.create_page_context()
        reset_password_request_widget = self.create_reset_password_request_widget()
        reset_password_request_widget.messages = messages.get_messages(self.request)
        page_context.add_widget(reset_password_request_widget)
        return HttpResponse(page_context.render())
    def POST(self):
        if not self.params['email']:
            messages.error(self.request, 'Email is required', extra_tags='email')
        if self.params['email'] and not re.match("[^@]+@[^@]+\.[^@]+", self.params['email']):
            messages.error(self.request, "Invalid email address", extra_tags='email')
        else:
            user = components.UserStore(self.get_container()).reset_password_request(self.params)['data']
            if user:
                link = helper.Helper().generate_reset_pass_link(self.request,user['user_id'], user['token'])
                helper.Helper().send_email(**{
                    'params': { 'username': user['username'], 'reset_link': link },
                    'subject': "Reset Genopedia Account Password Request",
                    'recievers': [user['email']],
                })
                messages.success(self.request, 'An email has been sent to {}'.format(self.params['email']), extra_tags='sent')
                return HttpResponseRedirect('/reset-password/sent')
            else:
                messages.error(self.request, 'Email is incorrect', extra_tags='email')
        page_context = self.create_page_context()
        reset_password_request_widget = self.create_reset_password_request_widget()
        reset_password_request_widget.messages = messages.get_messages(self.request)
        page_context.add_widget(reset_password_request_widget)
        reset_password_request_widget.form_data = self.params
        return HttpResponse(page_context.render())



class ResetPasswordRequestSent(common_actions.BaseAction):
    class ResetPasswordRequestSentWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class ResetPasswordRequestSentWidgetRenderer(renderers.BaseRenderer):
        def render(self, reset_password_request_sent):
            template = loader.get_template('genopedia/home/reset_password_request_sent.html')
            context = {}
            context['messages'] = reset_password_request_sent.messages
            return template.render(context)
    def create_reset_password_request_sent(self):
        reset_password_request_sent = self.ResetPasswordRequestSentWidget()
        reset_password_request_sent.renderer = self.ResetPasswordRequestSentWidgetRenderer()
        return reset_password_request_sent
    def GET(self):
        page_context = self.create_page_context()
        reset_password_request_sent = self.create_reset_password_request_sent()
        reset_password_request_sent.messages = messages.get_messages(self.request)
        page_context.add_widget(reset_password_request_sent)
        return HttpResponse(page_context.render())



class ResetPassword(common_actions.BaseAction):
    class ResetPasswordtWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class ResetPasswordtWidgetRenderer(renderers.BaseRenderer):
        def render(self, reset_password_widget):
            template = loader.get_template('genopedia/home/reset_password.html')
            context = {}
            context['id'] = reset_password_widget.id
            context['token'] = reset_password_widget.token
            context['messages'] = reset_password_widget.messages
            return template.render(context)
    def create_reset_password_widget(self, id, token):
        reset_password_widget = self.ResetPasswordtWidget()
        reset_password_widget.renderer = self.ResetPasswordtWidgetRenderer()
        reset_password_widget.messages = messages.get_messages(self.request)
        reset_password_widget.id = id
        reset_password_widget.token = token
        return reset_password_widget
    def GET(self):
        is_token_exists = components.UserStore(self.get_container()).check_reset_pass_token(self.params['id'], self.params['token'])['data']['record']
        if is_token_exists:
            page_context = self.create_page_context()
            reset_password_widget = self.create_reset_password_widget(self.params['id'], self.params['token'])
            page_context.add_widget(reset_password_widget)
            return HttpResponse(page_context.render())
        else:
            return helper.CommonPage().response_404(self.request)
    def POST(self):
        if not self.params['new_password']:
            messages.error(self.request, "New password is required", extra_tags='new_password')
        if not self.params['confirm_password']:
            messages.error(self.request, "Confirm new password is required", extra_tags='confirm_password')
        else:
            if len(self.params['new_password']) < 2:
                messages.error(self.request, "Password must be at least 2 characters", extra_tags='new_password')
            if self.params['confirm_password'].strip() != self.params['new_password'].strip():
                messages.error(self.request, "Confirm password is not match to password", extra_tags='confirm_password')
            else:
                user = components.UserStore(self.get_container()).reset_password_save(self.params)['data']
                user = components.UserStore(self.get_container()).profile(user['id'])['data']['record']
                if user:
                    return components.UserManager().refresh_user_cookie(user,self.request,'/user/profile')
                else:
                    messages.error(self.request, "Opps! Something went wrong, please try again", extra_tags='server-error')
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])



class Inbox(common_actions.BaseAction):
    class InboxWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class InboxtWidgetRenderer(renderers.BaseRenderer):
        def render(self, inbox_widget):
            template = loader.get_template('genopedia/home/inbox.html')
            context = {}
            context['inbox'] = json.dumps(inbox_widget.inbox)
            context['contact'] = inbox_widget.contact
            context['user_active'] = inbox_widget.user_active
            return template.render(context)
    def create_inbox_widget(self):
        inbox_widget = self.InboxWidget()
        inbox_widget.renderer = self.InboxtWidgetRenderer()
        return inbox_widget
    def GET(self):
        user = components.UserManager().parse_user(self.request)
        self.params['r'] = user['userid']
        page_context = self.create_page_context()
        inbox_widget = self.create_inbox_widget()
        inbox_widget.inbox =    components.UserStore(self.get_container()).get_inbox(self.params)['data']['record']
        inbox_widget.contact =  components.UserStore(self.get_container()).get_contact(self.params)['data']['record']
        inbox_widget.user_active = ''
        if 'u' in self.params:
            inbox_widget.user_active = self.params['u']
        page_context.add_widget(inbox_widget)
        return HttpResponse(page_context.render())
    def POST(self):
        user = components.UserManager().parse_user(self.request)
        data = {
            'sender_id': user['userid'],
            'receiver_id': self.params['selected_user_id'],
            'message':  self.params['message']
        }
        message = components.UserStore(self.get_container()).send_message(data)
        return HttpResponseRedirect('/user/inbox?u={}'.format(self.params['selected_user_name']))

class SendMessage(common_actions.BaseAction):
    def POST(self):
        user = components.UserManager().parse_user(self.request)
        data = {
            'sender_id': user['userid'],
            'receiver_id': self.params['selected_user_id'],
            'message':  self.params['message']
        }
        self.params['r'] = user['userid']
        self.params['u'] = self.params['selected_user_name']
        message = components.UserStore(self.get_container()).send_message(data)
        inbox = components.UserStore(self.get_container()).get_inbox(self.params)['data']['record']
        return JsonResponse(inbox)

class MessageRealtime(common_actions.BaseAction):
    def POST(self):
        user = components.UserManager().parse_user(self.request)
        self.params['r'] = user['userid']
        self.params['u'] = self.params['selected_user_name']
        inbox = components.UserStore(self.get_container()).get_inbox(self.params)['data']['record']
        return JsonResponse(inbox)

class ScienceFilter(common_actions.BaseAction):
    class ScienceFilterWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class ScienceFilterWidgetRenderer(renderers.BaseRenderer):
        def __init__(self):
            pass
        def render(self, data):
            template = loader.get_template('genopedia/home/science_filter.html')
            context = {}
            context['science_filter'] = data.science_filter
            return template.render(context)
    def create_widget(self):
        widget = self.ScienceFilterWidget()
        widget.renderer = self.ScienceFilterWidgetRenderer()
        return widget
    def GET(self):
        page_context = self.create_page_context()
        widget = self.create_widget()
        user = components.UserManager().parse_user(self.request)
        widget.science_filter = user['science_filter']
        page_context.add_widget(widget)
        return HttpResponse(page_context.render())

class Upload(common_actions.BaseAction):
    class UploadWidget(widgets.BaseWidget):
        def __init__(self):
            pass
    class UploadWidgetRenderer(renderers.BaseRenderer):
        def __init__(self):
            pass
        def render(self, sign_in_widget):
            template = loader.get_template('genopedia/home/upload.html')
            context = {}
            return template.render(context)
    def create_widget(self):
        widget = self.UploadWidget()
        widget.renderer = self.UploadWidgetRenderer()
        return widget
    def GET(self):
        page_context = self.create_page_context()
        widget = self.create_widget()
        page_context.add_widget(widget)
        return HttpResponse(page_context.render())

class UpdateVariation(common_actions.BaseAction):
    def POST(self):
        params = self.params
        user = components.UserManager().parse_user(self.request)
        params['user_id'] = user['userid']
        if 'file' in self.request.FILES:
            file = self.request.FILES['file']
            text = file.read()
            if text:
                components.UserStore(self.get_container()).user_upload({'text': text, 'user_id': user['userid']})
        if 'science_filter' in self.params:
            components.UserStore(self.get_container()).edit_profile(params)

        rs = components.UserStore(self.get_container()).profile(user['userid'])['data']['record']
        if rs:
            if 'file' in self.request.FILES:
                return components.UserManager().refresh_user_cookie(rs,self.request,'/user/upload')
            return components.UserManager().refresh_user_cookie(rs,self.request,'/user/science-filter')
        else:
            messages.error(self.request, "Opps! Something went wrong, please try again", extra_tags='server-error')
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
