from notasquare.urad_web.page_contexts import standard
from application.themes.genopedia import renderers
from application.modules.common import components as common_components

class FullPageContext(standard.FullPageContext):
    def __init__(self):
        super(FullPageContext, self).__init__()
        self.app_title = 'Genopedia'
        self.page_title = 'Genopedia'
        self.menu.create_menu_group('variation', 'Variation', '/variation/list', 'zmdi-format-subject')
        self.menu.create_menu_group('gene', 'Gene', '/gene/list', 'zmdi-format-subject')
        self.menu.create_menu_group('disease', 'Disease', '/disease/list', 'zmdi-format-subject')
        self.renderer = renderers.page_contexts.FullPageContextRenderer()
        self.messages = None

