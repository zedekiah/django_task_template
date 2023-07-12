import requests
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.transaction import atomic


class Command(BaseCommand):
    help = 'Заполняет базу фикстурами'

    @staticmethod
    def get_random_users(self, count=100) -> list[dict]:
        r = requests.get('https://randomuser.me/api/', params={'results': count})

        return r.json()['results']

    @atomic
    def handle(self, *args, **options) -> None:
        User.objects.all().delete()

        users: list[User] = []
        for user_data in self.get_random_users(1000):
            user = User(
                username=user_data['login']['username'],
                first_name=user_data['name']['first'],
                last_name=user_data['name']['last'],
                email=user_data['email'],
            )
            user.set_password('1234567890')
            users.append(user)

        User.objects.bulk_create(users)
