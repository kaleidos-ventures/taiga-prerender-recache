from django.core.management.base import BaseCommand, CommandError
from prerender_recache.service import process_scheduled_recaches


class Command(BaseCommand):
    help = 'Recache all pending pages'

    def handle(self, *args, **options):
        process_scheduled_recaches()
