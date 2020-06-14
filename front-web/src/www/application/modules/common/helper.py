from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

import uuid, os


class Helper(object):
    def uploader(self, f):
        try:
            prefix_name = "{}-{}".format(str(uuid.uuid4()).replace('-',''), f.name)
            path = "{}/{}".format(settings.MEDIA_ROOT, prefix_name)
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            # path = "{}/{}".format(settings.MEDIA_ROOT, prefix_name)
            with open(path, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            return prefix_name
        except Exception as e:
            return False

    def send_email(self, **data): 
        html_content = render_to_string('genopedia/home/reset_passwrod_mail_template.html', data['params'])
        email = EmailMultiAlternatives(data['subject'], settings.EMAIL_HOST_USER)
        email.attach_alternative(html_content, "text/html")
        email.to = data['recievers']
        email.send()

    def generate_reset_pass_link(self, request, user_id, token):
        host = 'http' + ('', 's')[request.is_secure()] + '://'+ request.META['HTTP_HOST']
        return '{}/reset-password/confirm?id={}&token={}'.format(host, user_id, token)



class CommonPage(object):
    def response_404(self, request):
        response = render_to_response('genopedia/home/404.html', {}, context_instance=RequestContext(request))
        response.status_code = 404
        return response