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
        def render_cell_actions(self, table, row):
            html  = '<div class="btn-group btn-group">'
            html += '    <a class="btn btn-xs btn-primary" href="/user/edit/%s">Edit</a>' % (row['id'])
            html += '    <a class="btn btn-xs btn-danger" href="/user/delete/%s" onclick="return confirm(\'Are you really want to delete this?\')">Delete</a>'  % (row['id'])
            html += '</div>'
            return html
    def create_table(self):
        table = widgets.table.DataTable()
        table.set_title('User')
        table.set_subtitle('List of users')
        table.create_button('create', '/user/create', 'zmdi-plus')
        table.create_detail_link('/user/summary/')
        table.create_column('id', 'ID', '6%', sortable=True)
        table.create_column('username', 'Username', '20%', sortable=True)
        table.create_column('email', 'Email', '20%', sortable=True)
        table.create_column('fullname', 'Name', '30%')
        table.create_column('actions', '', '14%')
        table.add_field(widgets.field.Textbox('username'))
        table.renderer = self.TableRenderer()
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('username', 'Username', colspan=12)
        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        return components.UserStore(self.get_container()).list(table_form_data, sortkey, sortdir, page_number)


class Create(actions.crud.CreateAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    def create_form(self):
        form = widgets.form.Form()
        form.set_title('User')
        form.add_field(widgets.field.Textbox('username'))
        form.add_field(widgets.field.Textbox('email'))
        form.add_field(widgets.field.Textbox('password'))
        form.add_field(widgets.field.Textbox('salt'))
        form.add_field(widgets.field.Textbox('fullname'))
        form.add_field(widgets.field.Textarea('about'))
        form.add_field(widgets.field.Combobox('gender', choices=constants.GENDER))
        form.add_field(widgets.field.Combobox('country', choices=constants.COUNTRIES))
        form.add_field(widgets.field.Combobox('education', choices=constants.EDUCATION))
        form.add_field(widgets.field.Textbox('work'))
        form.add_field(widgets.field.Textbox('birthday'))
        form.add_field(widgets.field.Textbox('account_paypal'))
        form.add_field(widgets.field.Combobox('science_filter', choices=constants.SCIENCE_FILTER))
        form.renderer = renderers.widgets.form.HorizontalFormRenderer()
        form.renderer.add_section('Account information')
        form.renderer.add_field('username', 'Username')
        form.renderer.add_field('email', 'Email')
        form.renderer.add_field('password', 'Password')
        form.renderer.add_field('salt', 'Salt')
        form.renderer.add_section('Profile')
        form.renderer.add_field('birthday', 'Birthday')
        form.renderer.add_field('fullname', 'Full name')
        form.renderer.add_field('about', 'About you')
        form.renderer.add_field('gender', 'Gender')
        form.renderer.add_field('country', 'Country')
        form.renderer.add_field('education', 'Education')
        form.renderer.add_field('work', 'Currently job')
        form.renderer.add_field('science_filter', 'Science filter')
        form.renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        form.renderer.set_field_renderer('textarea', renderers.widgets.field.TextareaRenderer())
        form.renderer.set_field_renderer('combobox', renderers.widgets.field.ComboboxRenderer())
        return form
    def load_form(self, form):
        form.set_form_data({
        })
    def process_form_data(self, data):
        return components.UserStore(self.get_container()).create(data)


class Edit(actions.crud.UpdateAction):
    def create_page_context(self):
        self.params['submenu'] = 'edit'
        return components.FullPageContext(self.params, self.container)
    def create_form(self):
        form = widgets.form.Form()
        form.set_title('User')
        form.add_field(widgets.field.Textbox('email'))
        form.add_field(widgets.field.Textbox('username'))
        form.add_field(widgets.field.Combobox('is_active', choices=constants.ACTIVE_STATUS))
        form.add_field(widgets.field.Textbox('fullname'))
        form.add_field(widgets.field.Textarea('about'))
        form.add_field(widgets.field.Textbox('position'))
        form.add_field(widgets.field.Combobox('gender', choices=constants.GENDER))
        form.add_field(widgets.field.Combobox('country', choices=constants.COUNTRIES))
        form.add_field(widgets.field.Combobox('education', choices=constants.EDUCATION))
        form.add_field(widgets.field.Textbox('work'))
        form.add_field(widgets.field.Textbox('rank'))
        form.add_field(widgets.field.Combobox('genetic_type_code', choices=constants.GENETIC_TYPE))
        form.add_field(widgets.field.Textbox('birthday'))
        form.add_field(widgets.field.Textbox('account_paypal'))
        form.add_field(widgets.field.Combobox('science_filter', choices=constants.SCIENCE_FILTER))

        form.renderer = renderers.widgets.form.HorizontalFormRenderer()
        form.renderer.add_section('User information')
        form.renderer.add_field('username', 'Username')
        form.renderer.add_field('email', 'Email')
        form.renderer.add_field('is_active', 'Active')

        form.renderer.add_section('User Profile')
        form.renderer.add_field('fullname', 'Fullname')
        form.renderer.add_field('about', 'About')
        form.renderer.add_field('position', 'Position')
        form.renderer.add_field('gender', 'Gender')
        form.renderer.add_field('country', 'Country')
        form.renderer.add_field('education', 'Education')
        form.renderer.add_field('work', 'Work')
        form.renderer.add_field('rank', 'Rank')
        form.renderer.add_field('genetic_type_code', 'Genetic Type')
        form.renderer.add_field('birthday', 'Birthday')
        form.renderer.add_field('account_paypal', 'Account Paypal')
        form.renderer.add_field('science_filter', 'Science filter')

        form.renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        form.renderer.set_field_renderer('textarea', renderers.widgets.field.TextareaRenderer())
        form.renderer.set_field_renderer('combobox', renderers.widgets.field.ComboboxRenderer())
        return form
    def load_form(self, form):
        result = components.UserStore(self.get_container()).summary(self.params['user_id'])
        if result['status'] == 'ok':
            record = result['data']['record']
            form.set_form_data(record)
        else:
            form.add_message('danger', "Can't load form")
    def process_form_data(self, data):
        data['user_id'] = self.params['user_id']
        return components.UserStore(self.get_container()).edit(data)


class Delete(actions.crud.DeleteAction):
    def GET(self):
        result = components.UserStore(self.get_container()).delete(self.params['user_id'])
        return HttpResponseRedirect('/user/list')

class Active(actions.crud.FormAction):
    def POST(self):
        result = components.UserStore(self.get_container()).active(self.params)['data']
        return HttpResponseRedirect('/user/summary/{}'.format(self.params['user_id']))


class Inactive(actions.crud.FormAction):
    def POST(self):
        result = components.UserStore(self.get_container()).inactive(self.params)['data']
        return HttpResponseRedirect('/user/summary/{}'.format(self.params['user_id']))


class Summary(actions.crud.FormAction):
    def create_page_context(self):
        self.params['submenu'] = 'summary'
        return components.FullPageContext(self.params, self.container)
    class UserSummaryRenderer(BaseRenderer):
        def render(self, datatable):
            template = loader.get_template('material/user/summary.html')
            context = {}
            context['user'] = datatable.data
            return template.render(context)
    def create_table(self):
        table = widgets.table.DataTable()
        table.renderer = self.UserSummaryRenderer()
        return table
    def load_table_data(self):
        return components.UserStore(self.get_container()).summary(self.params['user_id'])
    def GET(self):
        page_context = self.create_page_context()
        table_widget = self.create_table()
        data = self.load_table_data()
        data = data['data']['record']
        table_widget.set_data(data)
        page_context.add_widget(table_widget)
        return HttpResponse(page_context.render())

class File(actions.crud.UpdateAction):
    def create_page_context(self):
        self.params['submenu'] = 'file'
        return components.FullPageContext(self.params, self.container)
    class FileRenderer(BaseRenderer):
        def render(self, datatable):
            template = loader.get_template('material/user/upload.html')
            context = {}
            context['user_id'] = datatable.data['user_id']
            if 'alert' in datatable.data:
                context['alert'] = datatable.data['alert']
            if 'updated_at' in datatable.data:
                context['updated_at'] = datatable.data['updated_at']
            return template.render(context)
    def create_table(self):
        table = widgets.table.DataTable()
        table.renderer = self.FileRenderer()
        return table
    def load_table_data(self):
        return components.UserStore(self.get_container()).check_upload(self.params['user_id'])
    def GET(self):
        page_context = self.create_page_context()
        table_widget = self.create_table()
        data = self.load_table_data()['data']['record']
        table_widget.set_data(data)
        page_context.add_widget(table_widget)
        return HttpResponse(page_context.render())
    def POST(self):
        if 'file' in self.request.FILES:
            file = self.request.FILES['file']
            text = file.read()
            if text:
                rs = components.UserStore(self.get_container()).user_upload_edit({'text': text, 'user_id': self.params['user_id']})
                page_context = self.create_page_context()
                table_widget = self.create_table()
                data = {
                    'user_id': self.params['user_id'],
                    'alert': rs['status']
                }
                table_widget.set_data(data)
                page_context.add_widget(table_widget)
                return HttpResponse(page_context.render())

class FileRemove(actions.crud.FormAction):
    def GET(self):
        components.UserStore(self.get_container()).user_upload_remove(self.params['user_id'])
        return HttpResponseRedirect('/user/file/{}'.format(self.params['user_id']))

class Variation(actions.crud.ListAction):
    def create_page_context(self):
        self.params['submenu'] = 'variation'
        return components.FullPageContext(self.params, self.container)
    class TableRenderer(renderers.widgets.table.DataTableRenderer):
        def render_cell_actions(self, table, row):
            return ''
    def create_table(self):
        table = widgets.table.DataTable()
        table.set_title('User variation')
        table.create_column('id', 'ID', '6%', sortable=True)
        table.create_column('rsnumber', 'Rsnumber', '15%', sortable=True)
        table.create_column('chromosome', 'Chromosome', '15%')
        table.create_column('position', 'Position', '15%', sortable=True)
        table.create_column('genotype', 'Genotype', '15%')
        table.add_field(widgets.field.Textbox('rsnumber'))
        table.renderer = self.TableRenderer()
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('rsnumber', 'Rsnumber', colspan=8)
        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        return components.UserStore(self.get_container()).user_variation_get(table_form_data, sortkey, sortdir, page_number, self.params['user_id'])
