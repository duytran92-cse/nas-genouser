from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from notasquare.urad_web import actions, page_contexts, widgets
from notasquare.urad_web_material import renderers
from application import constants
from django.template import loader
from notasquare.urad_web.renderers import BaseRenderer
from . import components


class List(actions.crud.ListAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    class TableRenderer(renderers.widgets.table.DataTableRenderer):
        pass
    def create_table(self):
        table = widgets.table.DataTable()
        table.set_title('User')
        table.set_subtitle('List of users')
        table.create_button('create', '/user/create', 'zmdi-plus')
        table.create_detail_link('/inbox/messages/')
        table.create_column('id', 'ID', '6%', sortable=True)
        table.create_column('sender', 'sender', '20%', sortable=True)
        table.create_column('receiver', 'Receiver', '20%', sortable=True)
        table.create_column('when', 'Sent at', '30%')
        table.create_column('actions', '', '14%')
        table.add_field(widgets.field.Textbox('sender'))
        table.add_field(widgets.field.Textbox('receiver'))
        table.renderer = self.TableRenderer()
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('sender', 'Sender', colspan=6)
        table.renderer.table_form_renderer.add_field('receiver', 'Receiver', colspan=6)
        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        return components.InboxStore(self.get_container()).list(table_form_data, sortkey, sortdir, page_number)



class Detail(actions.crud.FormAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    class DetailRenderer(BaseRenderer):
        def render(self, datatable):
            template = loader.get_template('material/inbox/detail.html')
            context = {}
            context['messages'] = datatable.data
            return template.render(context)
    def create_table(self):
        table = widgets.table.DataTable()
        table.renderer = self.DetailRenderer()
        return table
    def load_table_data(self):
        return components.InboxStore(self.get_container()).list(params=self.params)
    def GET(self):
        page_context = self.create_page_context()
        table_widget = self.create_table()
        data = self.load_table_data()
        data = data['records']
        table_widget.set_data(data)
        page_context.add_widget(table_widget)
        return HttpResponse(page_context.render())