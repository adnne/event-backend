from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField, 
    EmailField, 
    ImageField
)
from model_utils.models import TimeStampedModel

class User(AbstractUser,TimeStampedModel):
    username = CharField("Last name", blank=True, null=True, max_length=255)
    profile_image = ImageField(upload_to='users', blank=True, null=True)
    last_name = CharField("Last name", blank=True, null=True, max_length=255)
    full_name = CharField("Full name", blank=True, null=True, max_length=255)
    email = EmailField("Email address", unique=True, blank=True, null=True)
    phone_number = CharField("Phone number", blank=True, max_length=255, null=True)
