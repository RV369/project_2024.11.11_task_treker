import random
from django.contrib.auth.models import User

users_count = User.objects.count()


def employee_selection():
    return random.randint(1, users_count)

