from django.template import loader
from notasquare.urad_web.renderers import BaseRenderer

class DashboardRenderer(BaseRenderer):
    def __init__(self):
        super(DashboardRenderer, self).__init__()
        self.template = 'material/dashboard/dashboard.html'
    def render(self, table):
        template = loader.get_template(self.template)
        context = {}
        context['statistic'] = table.data
        return template.render(context)
