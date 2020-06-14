from django.conf import settings
from application.modules.common import page_contexts

class ApplicationSettingStore(object):
    def __init__(self, container):
        self.container = container
    def get(self):
        return self.container.call_api(settings.USER_API_URL + '/application_setting/get', GET={})
    def update(self, data):
        return self.container.call_api(settings.USER_API_URL + '/application_setting/update', POST=data)

class PageFullPageContext(page_contexts.FullPageContext):
    def __init__(self, params):
        super(PageFullPageContext, self).__init__()
        self.menu.set_group_selected('application_setting')
