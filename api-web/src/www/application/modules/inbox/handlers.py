from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from notasquare.urad_api import *
from application.models import *
from application import constants
from application.helpers.shortnaturaltime import shortnaturaltime



class List(handlers.standard.ListHandler):
    def create_query(self, data):
        query = UserMessage.objects
        if data.get('sender', ''):
            query = query.filter(sender_id__username__istartswith=data['sender'])
        if data.get('receiver', ''):
            query = query.filter(receiver_id__username__istartswith=data['receiver'])
        if data.get('inbox_id', ''):
            query = query.filter(pk=data['inbox_id'])
        return query
    def serialize_entry(self, inbox):
        return {
            'id':           inbox.id,
            'sender':       inbox.sender.username,
            'receiver':     inbox.receiver.username,
            'message':      inbox.message,
            'when':         inbox.sent_at.strftime("%m/%d/%Y %H:%M:%S"),
        }

class Contact(handlers.standard.GetHandler):
    def get_data(self, data):
        records = []
        if data.get('r', '') != '':
            for c in UserContact.objects.filter(Q(user_id=data['r'])):
                records.append({
                    'username': c.friend.username,
                    'photo': c.friend.userprofile.photo,
                    'num_of_new_messages': UserMessage.objects.filter(sender_id=c.friend_id, receiver_id=c.user_id, is_read=False).count()
                })
        if data.get('qu', '') != '':
            records = []
            for c in User.objects.filter(username__istartswith=data['qu']).exclude(pk=data['r']):
                records.append({
                    'username': c.username,
                    'photo': c.userprofile.photo,
                })
        return records

class Inbox(handlers.standard.GetHandler):
    def get_data(self, data):
        records = { 'messages': [], 'selected_user': None }
        if data.get('u', '') != '':
            sender = User.objects.get(username=data['u'])
            query = UserMessage.objects.filter(Q(sender_id=sender.id, receiver_id=data['r']) | Q(sender_id=data['r'], receiver_id=sender.id)).order_by('sent_at')
            records['selected_user'] = {'username': sender.username, 'id': sender.id, 'photo': sender.userprofile.photo}
            u_before = ''
            for record in query:
                records['messages'].append({
                    'sender_photo': record.sender.userprofile.photo,
                    'sender':   record.sender.username,
                    'message':  record.message,
                    'when':     shortnaturaltime(record.sent_at),
                    'user_before': u_before
                })
                u_before = record.sender.username
                if int(data['r']) == int(record.receiver_id):
                    record.is_read = True
                    record.save()
        return records


class SendMessage(handlers.standard.CreateHandler):
    def create(self, data):
        user_message = UserMessage(sender_id=data['sender_id'], receiver_id=data['receiver_id'], message=data['message'])
        user_message.save()
        if UserContact.objects.filter(user_id=data['sender_id'], friend_id=data['receiver_id']).exists() == False:
            contact = UserContact(user_id=data['sender_id'], friend_id=data['receiver_id'])
            contact.save()
        if UserContact.objects.filter(user_id=data['receiver_id'], friend_id=data['sender_id']).exists() == False:
            contact = UserContact(user_id=data['receiver_id'], friend_id=data['sender_id'])
            contact.save()
        # Add notification
        user_noti = UserNotification()
        user_noti.user_id = data['receiver_id']
        user_noti.kind = 'message'
        user_noti.message = 'New message arrived'
        user_noti.save()
        return user_message
