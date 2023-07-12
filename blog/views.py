from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def users(request: HttpRequest) -> HttpResponse:
    user_list: list[User] = list(User.objects.all())

    return render(request, 'blog/users.html', context={'user_list': user_list})
