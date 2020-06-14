from django.conf import settings
from application.modules.common import page_contexts

class UserStore(object):
    def __init__(self, container):
        self.container = container
    def list(self, params={}, sortkey='id', sortdir='desc', page_number=1):
        params['_pager_start'] = (page_number - 1) * 10
        params['_pager_num'] = 10
        params['_sort_key'] = sortkey
        params['_sort_dir'] = sortdir
        data = self.container.call_api(settings.USER_API_URL + '/user/list', GET=params)
        return data['data']
    def get(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user/get', GET={'id': id})
    def summary(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user/summary', GET={'id': id})
    def create(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/create', POST=data)
    def edit(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/edit', POST=data)
    def active(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/active', POST=data)
    def inactive(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user/inactive', POST=data)
    def delete(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user/delete', POST={'user_id': id})
    def user_upload_get(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user-upload/get', GET={'user_id': id})
    def user_variation_get(self, params={}, sortkey='id', sortdir='desc', page_number=1, id=""):
        params['_pager_start'] = (page_number - 1) * 10
        params['_pager_num'] = 10
        params['_sort_key'] = sortkey
        params['_sort_dir'] = sortdir
        params['user_id'] = id
        data = self.container.call_api(settings.USER_API_URL + '/user-variation/get', GET=params)
        return data['data']
    def user_variation_update(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user-variation/update', POST=data)
    def user_upload_edit(self, data):
        return self.container.call_api(settings.USER_API_URL + '/user-upload/edit', POST=data)
    def check_upload(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user-upload/check_upload', GET={'user_id': id})
    def user_upload_remove(self, id):
        return self.container.call_api(settings.USER_API_URL + '/user-upload/delete', GET={'user_id': id})
    def populate_combobox(self):
        choices = []
        params = {}
        records = self.list(sortkey='name', sortdir='asc', params=params)
        for record in records['records']:
            choices.append({
                'id':     record['id'],
                'label':  record['name']
            })
        return choices



class FullPageContext(page_contexts.FullPageContext):
    def __init__(self, params, container):
        super(FullPageContext, self).__init__(container.request)
        self.page_title = 'User'
        self.menu.set_group_selected('user')

        self.breadcrumb.add_entry('user', 'User', '/user/list')

        if 'user_id' in params and params['user_id']:
            self.submenu.create_menu_group('summary', 'Summary', '/user/summary/%s' % (str(params['user_id'])), 'zmdi-border-all')
            self.submenu.create_menu_group('edit', 'Edit', '/user/edit/%s' % (str(params['user_id'])), 'zmdi-border-all')
            self.submenu.create_menu_group('file', 'File uploaded', '/user/file/%s' % (str(params['user_id'])), 'zmdi-border-all')
            self.submenu.create_menu_group('variation', 'Variation', '/user/variation/%s' % (str(params['user_id'])), 'zmdi-border-all')
            self.submenu.set_group_selected(params['submenu'])
