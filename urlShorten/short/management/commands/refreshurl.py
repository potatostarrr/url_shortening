from django.core.management.base import BaseCommand,CommandError
from short.models import NewURL

class Command(BaseCommand):
    help = 'refresh all'

    def add_arguments(self, parser):
        parser.add_argument('items',  type=int)

    def handle(self, *args, **options):
        return NewURL.objects.refresh_url(items=options['number'])
