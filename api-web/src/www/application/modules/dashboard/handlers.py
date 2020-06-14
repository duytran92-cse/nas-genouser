from notasquare.urad_api import *
from application.models import *


class Dashboard(handlers.standard.GetHandler):
    def get_data(self, data):
        links = []
        user_records = User.objects.all().count()
        links.append({
            'link': '/user/list',
            'tags': str(user_records),
            'title': 'Total Users',
        })
        return links
