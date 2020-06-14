from django.conf import settings

# class ApplicationSettingStore(object):
#     def __init__(self, container):
#         self.container = container
#     def get(self):
#         return self.container.call_api(settings.NOTASQUARE_API_URL + '/application_setting/get', GET={})


# class PageStore(object):
#     def __init__(self, container):
#         self.container = container    
#     def get(self, id):
#         return self.container.call_api(settings.NOTASQUARE_API_URL + '/page/get', GET={'id': id})