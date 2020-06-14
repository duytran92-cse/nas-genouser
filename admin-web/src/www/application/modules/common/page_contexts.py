from django.conf import settings
from notasquare.urad_web.page_contexts import standard
from notasquare.urad_web_material import renderers
import urllib

class FullPageContext(standard.FullPageContext):
    def __init__(self,request):
        super(FullPageContext, self).__init__()
        self.app_title = 'User'
        self.page_title = 'User'
        self.breadcrumb.add_entry('home', 'Dashboard', '/')
        self.menu.create_menu_group('dashboard', 'Dashboard', '/dashboard', 'zmdi-format-subject')
        self.menu.create_menu_group('user', 'User', '/user/list', 'zmdi-format-subject')
        self.menu.create_menu_group('inbox', 'Inbox', '/inbox/list', 'zmdi-format-subject')
        self.renderer = renderers.page_contexts.FullPageContextRenderer()

        # User
        self.user = request.META['USER']
        self.user['logout_link'] = settings.SECURITY_SERVER_URL + '/user/logout?redirect=%s' % (settings.APPLICATION_URL)
