from django.core.management import BaseCommand
from apps.rest_api.models import Group
from apps.chat.models import Room

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        groups = Group.objects.all()
        for group in groups:
            Room.objects.get_or_create(group=group, owner=group.owner)
