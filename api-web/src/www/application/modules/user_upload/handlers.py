from django.db.models import Q
from notasquare.urad_api import *
from application.models import *
from application import constants
import string


class Get(handlers.standard.GetHandler):
    def get_data(self, data):
        if 'user_id' in data and data['user_id']:
            try:
                data = UserUpload.objects.filter(user_id=data['user_id'], is_disable=False)
                return {
                    'id':               data[0].id,
                    'user_id':          data[0].user_id,
                    'text':             data[0].text,
                    'updated_at':       data[0].updated_at,
                }
            except UserUpload.DoesNotExist:
                return None

class CheckUpload(handlers.standard.GetHandler):
    def get_data(self, data):
        if 'user_id' in data and data['user_id']:
            rs = UserUpload.objects.filter(is_disable=False, user_id=data['user_id'])
            if rs:
                return {
                    'user_id': data['user_id'],
                    'updated_at': rs[0].updated_at
                }
        return {'user_id': data['user_id']}


class Edit(handlers.standard.UpdateHandler):
    def update(self, data):
        UserUpload.objects.filter(user_id=data['user_id'], is_disable=False).update(is_disable=True)
        user = UserUpload()
        user.user_id = data['user_id']
        user.save()
        if data.get('text', ''):
            # Update user variation
            line = data['text'].split("\n")
            if len(line) > 0:
                UserVariation.objects.filter(user_id=data['user_id']).delete()
                users = []
                for li in line:
                    if li:
                        if li[0] != '#':
                            tokens = li.split("\t")
                            if len(tokens) == 4:
                                user = UserVariation()
                                user.user_id = data['user_id']
                                user.rsnumber = tokens[0]
                                user.chromosome = tokens[1]
                                user.position = tokens[2]
                                user.genotype = tokens[3]
                                users.append(user)
                if users:
                    start = 0
                    end = 0
                    while end <= len(users):
                        end = start + 10000
                        UserVariation.objects.bulk_create(users[start:end])
                        start = end
                print 'DONE'
        return user


class Delete(handlers.standard.GetHandler):
    def get_data(self, data):
        UserUpload.objects.filter(user_id=data['user_id'], is_disable=False).update(is_disable=True)
        UserVariation.objects.filter(user_id=data['user_id']).delete()
        return {'status': 'ok'}
