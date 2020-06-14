from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from notasquare.urad_web import actions, widgets
from application.themes.genopedia import renderers
from application.modules.common import page_contexts, components as common_components
from application import constants
from application.modules.user import components

class BaseAction(actions.BaseAction):
    def create_page_context(self):
        page_context = page_contexts.FullPageContext()
        page_context.user = components.UserManager().parse_user(self.request)
        page_context.messages = messages.get_messages(self.request)
        page_context.messages.used = True
        return page_context
