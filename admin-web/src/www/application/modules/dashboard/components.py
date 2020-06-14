from django.conf import settings
from application.modules.common import page_contexts

class DashboardStore(object):
    def __init__(self, container):
        self.container = container
    def list(self):
        data = self.container.call_api(settings.USER_API_URL + '/dashboard/statistic')
        return data['data']

     
class FullPageContext(page_contexts.FullPageContext):
    def __init__(self, params, container):
        super(FullPageContext, self).__init__(container.request)
        self.page_title = 'Dashboard'
        self.menu.set_group_selected('dashboard')
        