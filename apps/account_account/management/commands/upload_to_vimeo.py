from django.core.management import BaseCommand

from apps.app.models import Lecture
from apps.rest_api.vimeo_service import upload, upload_upload_all


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        upload(1, 2)
