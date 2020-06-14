from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import loader
from notasquare.urad_web import actions, widgets, renderers
from application.themes.genopedia import renderers as genopedia_renderers
from application.modules.common import page_contexts, actions as common_actions, components as common_components
from application import constants

class Home(common_actions.BaseAction):
    class StatisticsWidget(widgets.BaseWidget):
        def __init__(self):
            self.num_user = 0
    class StatisticsWidgetRenderer(renderers.BaseRenderer):
        def render(self, statistics_widget):
            template = loader.get_template('genopedia/home/statistics.html')
            context = {}
            return template.render(context)
    def create_statistics_widget(self):
        statistics_widget = self.StatisticsWidget()
        statistics_widget.renderer = self.StatisticsWidgetRenderer()
        return statistics_widget
    def GET(self):
        page_context = self.create_page_context()
        statistics_widget = self.create_statistics_widget()
        page_context.add_widget(statistics_widget)
        return HttpResponse(page_context.render())







