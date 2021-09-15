import random

from django.core.management.base import BaseCommand, CommandError

from apps.account_account.models import CustomUser
from apps.rest_api.models import Center, Connection, Group


def usernameGen(names):
    names = names.split(" ")
    for i in range(1, 1000):
        first_letter = names[0][0]
        three_letter = names[-1][:3]
        number = "{:03d}".format(random.randrange(1, 1000))
        username = first_letter + three_letter + number

        try:
            CustomUser.objects.get(username=username)
            return usernameGen("PMK GAC")
        except CustomUser.DoesNotExist:
            return username


# python manage.py add_many_users --counts 100 --center 1 --group 1
class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--counts", type=int)
        parser.add_argument("--group_id", type=int)
        parser.add_argument("--center_id", type=int)

    def handle(self, *args, **options):
        center_id = options["center_id"]
        group_id = options["group_id"]
        counts = options["counts"]
        if center_id and group_id:
            self.stdout.write(
                f"Creating random users and adding these users to center with id={center_id} adding them to group with id {group_id}"
            )
            if Center.objects.filter(id=options["center_id"]):
                center = Center.objects.get(id=options["center_id"])
                if Group.objects.filter(center=center, id=options["group_id"]):
                    group = Group.objects.filter(center=center, id=options["group_id"])[
                        0
                    ]
                    for counter in range(options["counts"]):
                        student = CustomUser.objects.create(
                            username=usernameGen("asd JKASDF JASDkad")
                        )
                        Connection.objects.create(
                            user=student,
                            center=center,
                            status="student",
                            is_verified=True,
                        )
                        group.students.add(student)
                        group.save()
        elif center_id and not group_id:
            self.stdout.write(
                f"Creating random users and adding these users to center with id={center_id}"
            )
            if Center.objects.filter(id=options["center_id"]):
                center = Center.objects.get(id=options["center_id"])
                for counter in range(options["counts"]):
                    student = CustomUser.objects.create(
                        username=usernameGen("asd JKASDF JASDkad")
                    )
                    Connection.objects.create(
                        user=student, center=center, status="student", is_verified=True
                    )
        else:
            self.stdout.write("Creating only random users")
            for counter in range(options["counts"]):
                CustomUser.objects.create(username=usernameGen("asd JKASDF JASDkad"))
