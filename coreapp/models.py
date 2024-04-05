from django.db import models
from django.contrib.auth.models import User

class User(User):
    authorization_status = models.CharField(max_length=255, blank=True, null=True)




