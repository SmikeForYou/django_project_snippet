from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        admins = settings.SUPERADMINS
        for email, username, password in admins:
            if not User.objects.filter(username=username).exists():
                u = User.objects.create_superuser(
                    email=email, username=username, password=password
                )
                u.save()
                print(f"User {username} successfully created")
            else:
                print(f'User "{username}" already exists')
