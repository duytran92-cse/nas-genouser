from notasquare.urad_api import *
from application.models import *
from application import constants


class Get(handlers.standard.GetHandler):
    def get_application_setting(self):
        records = ApplicationSetting.objects.all()
        for r in records:
            return r
        application_setting = ApplicationSetting()
        application_setting.save()
        return application_setting
    def get_data(self, data):
        application_setting = self.get_application_setting()
        return self.container.model_to_dict(application_setting)


class Update(handlers.standard.UpdateHandler):
    def parse_and_validate(self, params):
        parser = self.container.create_parser(params)
        if 'application_title' in params:
            if not parser.parse('application_title', 'string'):
                self.add_error('application_title', 'MUST_NOT_BE_EMPTY')
        return parser.get_data()
    def get_application_setting(self):
        records = ApplicationSetting.objects.all()
        for r in records:
            return r
        application_setting = ApplicationSetting()
        application_setting.save()
        return application_setting
    def update(self, data):
        application_setting = self.get_application_setting()
        if 'application_title' in data:
            application_setting.application_title = data['application_title']
        if 'contact_address_text' in data:
            application_setting.contact_address_text = data['contact_address_text']
        if 'about_genopedia_text' in data:
            application_setting.about_genopedia_text = data['about_genopedia_text']
        if 'facebook_url' in data:
            application_setting.facebook_url = data['facebook_url']
        if 'twitter_url' in data:
            application_setting.twitter_url = data['twitter_url']
        if 'youtube_url' in data:
            application_setting.youtube_url = data['youtube_url']
        if 'linkedin_url' in data:
            application_setting.linkedin_url = data['linkedin_url']
        if 'google_plus_url' in data:
            application_setting.google_plus_url = data['google_plus_url']
        if 'copyright_page' in data:
            application_setting.copyright_page_id = data['copyright_page']
        if 'impression_page' in data:
            application_setting.impression_page_id = data['impression_page']
        if 'privacy_page' in data:
            application_setting.privacy_page_id = data['privacy_page']
        if 'term_of_use_page' in data:
            application_setting.term_of_use_page_id = data['term_of_use_page']
        if 'stat_num_variation' in data:
            application_setting.stat_num_variation = data['stat_num_variation']
        if 'stat_num_gene' in data:
            application_setting.stat_num_gene = data['stat_num_gene']
        if 'stat_num_variation' in data:
            application_setting.stat_num_variation = data['stat_num_variation']
        if 'stat_num_disease' in data:
            application_setting.stat_num_disease = data['stat_num_disease']
        if 'stat_num_disease_causing_mutation' in data:
            application_setting.stat_num_disease_causing_mutation = data['stat_num_disease_causing_mutation']
        if 'stat_num_trait' in data:
            application_setting.stat_num_trait = data['stat_num_trait']
        if 'stat_num_drug' in data:
            application_setting.stat_num_drug = data['stat_num_drug']
        if 'stat_num_treatment' in data:
            application_setting.stat_num_treatment = data['stat_num_treatment']
        if 'stat_num_cited_publication' in data:
            application_setting.stat_num_cited_publication = data['stat_num_cited_publication']
        if 'stat_num_page' in data:
            application_setting.stat_num_page = data['stat_num_page']
        if 'stat_num_registered_user' in data:
            application_setting.stat_num_registered_user = data['stat_num_registered_user']
        if 'stat_num_genetic_code_letter' in data:
            application_setting.stat_num_genetic_code_letter = data['stat_num_genetic_code_letter']
        if 'stat_num_forum_post' in data:
            application_setting.stat_num_forum_post = data['stat_num_forum_post']
        application_setting.save()
        return application_setting
