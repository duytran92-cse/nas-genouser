from django.template import loader
from django.conf import settings
from notasquare.urad_web.renderers import BaseRenderer

class FullPageContextRenderer(BaseRenderer):
    def __init__(self):
        super(FullPageContextRenderer, self).__init__()
        self.template = 'genopedia/page_contexts/full.html'
    def render(self, full_page_context):
        template = loader.get_template(self.template)
        context = {}
        context['user'] =    full_page_context.user
        context['messages'] =   full_page_context.messages
        context['var_page'] =   settings.VARIATION_URL
        context['gene_page'] =   settings.GENE_URL
        context['dis_page'] =   settings.DISEASE_URL
        context['trait_page'] =   settings.TRAIT_URL
        context['treat_page'] =   settings.TREATMENT_URL
        context['gene_forum_page'] =   settings.GENE_FORUM_URL
        context['genebay_page'] =   settings.GENE_BAY_URL
        context['genome_browser_page'] = settings.GENOME_BROWSER_FRONTEND_URL
        context['frontSetting'] = {
            'impressionUrl' : settings.GENOME_BROWSER_FRONTEND_URL+ '/impression',
            'termOfUseUrl' : settings.GENOME_BROWSER_FRONTEND_URL+ '/term-of-use',
            'privacyPolicyUrl' : settings.GENOME_BROWSER_FRONTEND_URL+ '/privacy',
            'copyrightUrl' : settings.GENOME_BROWSER_FRONTEND_URL+ '/copyright',
        }
        context['social_network_url'] = {
            'facebook' : '',
            'twitter' : '',
            'youtube' : '',
            'linkedin' : '',
            'google_plus' : '',
        }
        widget_html = ''
        for widget in full_page_context.widgets:
            widget_html += widget.render()
        context['widget_html'] = widget_html

        return template.render(context)
