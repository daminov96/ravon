from django.core.management import BaseCommand
from apps.app.models import Day, Month, Year
from apps.app.modules import day_choices


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        months = Month.objects.all()
        for month in months:
            if not month.days.count():
                for i in day_choices():
                    Day.objects.create(day=i[1], month=month)
