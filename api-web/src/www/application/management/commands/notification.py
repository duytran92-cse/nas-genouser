from django.core.management.base import BaseCommand, CommandError
from application.models import *
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

class Command(BaseCommand):
    def handle(self, *args, **options):
        mess = {}
        user_noti = UserNotification.objects.filter(is_sent=False)
        for noti in user_noti:
            user = User.objects.get(pk=noti.user_id)
            if noti.user_id in mess:
                mess[noti.user_id]['noti'].append({
                    'kind': noti.kind,
                    'message': noti.message
                })
            else:
                mess[noti.user_id] = {
                    'username': user.username,
                    'email': user.email,
                    'noti': [{
                        'kind': noti.kind,
                        'message': noti.message
                    }]
                }

        if len(mess) > 0:
            title = 'You have new notifications'
            for i in mess:
                template = get_template('mail_noti.html')
                context = {}
                context['link'] = settings.FRONT_URL
                context['data'] = mess[i]['noti']
                content = template.render(context)
                mail = EmailMultiAlternatives(title, content, settings.EMAIL_HOST_USER, [mess[i]['email']])
                mail.attach_alternative(content, "text/html")
                mail.send()
                UserNotification.objects.filter(is_sent=False, user_id=i).update(is_sent=True)
                print "DONE"
