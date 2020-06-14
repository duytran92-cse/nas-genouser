from django.core.management.base import BaseCommand, CommandError
from application.models import *
from django.conf import settings
import json, pika, os

class Command(BaseCommand):
    def insert_variation(self, data):
        variation = Variation()
        variation.rsnumber = data['rsnumber']
        variation.position = data['position']
        variation.chromosome = data['chromosome']
        variation.science_filter = data['science_filter']
        variation.genes = data.get('genes', '')
        variation.publications = data.get('publications', '')
        variation.diseases = data.get('diseases', '')
        variation.effects = data.get('effects', '')
        variation.save()

    def consume(self, ch, method, properties, body):
        data = json.loads(body)
        self.insert_variation(data)

    def handle(self, *args, **options):
        credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
        connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST, settings.RABBITMQ_PORT, '/', credentials))

        channel = connection.channel()
        channel.queue_declare(queue='user-variation')
        channel.basic_consume(self.consume, queue='user-variation', no_ack=True)
        channel.start_consuming()
