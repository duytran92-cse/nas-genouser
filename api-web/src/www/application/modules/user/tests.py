import json
from django.utils.module_loading import import_string
from notasquare.urad_api import tests
from notasquare.urad_api.models import *

class UnitTest(tests.BaseUnitTest):
    def setUp(self):
        User.objects.create(name="User #1")
        User.objects.create(name="User #2")
        pass

    def test_basic(self):
        self.init()
        self.set_headers({
            'NAS-TEST-USER-ID':       1,
            'NAS-TEST-USER-USERNAME': 'vaquan'
        })
        self.get ('List all users', '/user/list')
        self.post('Create new user', '/user/create', {
            'name': 'New user',
        })
        self.post('Create new user (empty)', '/user/create', {
        })
        self.post('Create new user (empty 2)', '/user/create', {
            'name': '',
        })
        self.get('GET user id=3', '/user/get?id=3')
        self.get ('List all users', '/user/list')
        self.post('Update user id=3', '/user/update', {
            'id': 3,
            'name': 'User (updated)'
        })
        self.post('Update user id=2', '/user/update', {
            'id': 2,
            'name': ''
        })
        self.get ('List all users', '/user/list')
        self.post('Delete user id=1', '/user/delete', {
            'id': 1
        })
        self.get ('List all users', '/user/list')
