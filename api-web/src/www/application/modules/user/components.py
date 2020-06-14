from application.models import *

class ExtraUserHelper(object):
    def get_private_result(self, id):
        rs2 = UserUpload.objects.filter(is_disable=False, user_id=id)
        if rs2:
            private_result = 'active'
        else:
            private_result = ''
        return private_result
