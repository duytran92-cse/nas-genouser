from django.db.models import Q
from notasquare.urad_api import *
from application.models import *
from application import constants

class List(handlers.standard.ListHandler):
    def GET(self, data):
        rs = []
        query = UserVariation.objects
        if 'user_id' in data:
            query = query.filter(user_id=data['user_id'])

        if 'effect_filter' in data:
            if data['effect_filter'] == 'has_effect_on_me':
                vari = []
                for v in query:
                    vari.append(v.rsnumber)
                var = Variation.objects.filter(rsnumber__in=vari).exclude(effects__isnull=True).exclude(effects__exact='')
                if var:
                    rs = []
                    for r in var:
                        rs.append(r.rsnumber)
                if rs:
                    query = query.filter(rsnumber__in=rs)
        for i in query:
            varia = Variation.objects.filter(rsnumber=i.rsnumber)
            if varia:
                effects = varia[0].effects
            else:
                effects = ''
            rs.append({
                'id':               i.id,
                'user_id':          i.user_id,
                'rsnumber':         i.rsnumber,
                'position':         i.position,
                'chromosome':       i.chromosome,
                'genotype':         i.genotype,
                'effects':          effects
            })
        return ('ok', {'records': rs})

class GetVariation(handlers.standard.ListHandler):
    def GET(self, data):
        rs = []
        query = UserVariation.objects
        if 'user_id' in data:
            query = query.filter(user_id=data['user_id'])
        if 'rsnumber' in data:
            query = query.filter(rsnumber=data['rsnumber'])
        for i in query:
            varia = Variation.objects.filter(rsnumber=i.rsnumber)
            if varia:
                effects = varia[0].effects
            else:
                effects = ''
            rs.append({
                'id':               i.id,
                'user_id':          i.user_id,
                'rsnumber':         i.rsnumber,
                'position':         i.position,
                'chromosome':       i.chromosome,
                'genotype':         i.genotype,
                'effects':          effects
            })
        return ('ok', {'records': rs})


# class Get(handlers.standard.GetHandler):
#     def get_data(self, data):
#         info = []
#         if 'user_id' in data and data['user_id']:
#             try:
#                 data = UserVariation.objects.filter(user_id=data['user_id'])
#                 for item in data:
#                     info.append({
#                         'position': item.position,
#                         'chromosome': item.chromosome,
#                         'genotype': item.genotype,
#                         'rsnumber': item.rsnumber
#                     })
#                 return {
#                     'id':               data[0].id,
#                     'user_id':          data[0].user_id,
#                     'information':      info,
#                 }
#             except UserVariation.DoesNotExist:
#                 return None

class Get(handlers.standard.ListHandler):
    def create_query(self, data):
        query = UserVariation.objects
        if data.get('user_id', '') != '' :
            query = query.filter(user_id=data['user_id'])
        if data.get('rsnumber', '') != '' :
            query = query.filter(rsnumber=data['rsnumber'])
        return query
    def serialize_entry(self, user):
        return {
            'id':               user.id,
            'user_id':          user.user_id,
            'rsnumber':         user.rsnumber,
            'chromosome':       user.chromosome,
            'position':         user.chromosome,
            'genotype':         user.genotype,
        }

# class Create(handlers.standard.CreateHandler):
#     def create(self, data):
#         user_variation = UserVariation()
#         user_variation.user_id = data['user_id']
#         user_variation.rsnumber = data['rsnumber']
#         user_variation.position = data['position']
#         user_variation.chromosome = data['chromosome']
#         user_variation.genes = data['genes']
#         user_variation.publications = data['publications']
#         user_variation.diseases = data['diseases']
#         user_variation.genotype = data['genotype']
#         user_variation.save()
#         return user



class Edit(handlers.standard.UpdateHandler):
    def update(self, data):
        rs = UserVariation.objects.filter(user_id=data['user_id'])
        if rs:
            user = UserVariation.objects.get(pk=rs[0].id)
        else:
            user = UserVariation()

        if data.get('user_id', ''):
            user.user_id = data.get('user_id')
        if data.get('rsnumber', ''):
            user.rsnumber = data.get('rsnumber')
        if data.get('position', ''):
            user.position = data.get('position')
        if data.get('chromosome', ''):
            user.chromosome = data.get('chromosome')
        if data.get('genotype', ''):
            user.genotype = data.get('genotype')
        user.save()

        return user

class Update(handlers.standard.UpdateHandler):
    def update(self, data):
        rs = UserVariation.objects.filter(user_id=data['user_id'])
        if rs:
            UserVariation.objects.filter(user_id=data['user_id']).delete()

            if data.get('information', ''):
                for i in data['information']:
                    user = UserVariation()
                    user.user_id = int(data['user_id'])
                    user.rsnumber = i['rsnumber']
                    user.chromosome = i['chromosome']
                    user.position = i['position']
                    user.genotype = i['genotype']
                    user.save()
                return user
        return None


class Delete(handlers.standard.DeleteHandler):
    def delete(self, data):
        user = UserVariation.objects.get(pk=data['id'])
        user.delete()
        return 1
