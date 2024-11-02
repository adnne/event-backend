from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

User = get_user_model()



class Event(TimeStampedModel):
    image = models.ImageField(upload_to='events', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_limit = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created'] 

class RSVP(TimeStampedModel):
    RSVP_CHOICES = [
        ('ATTENDING', 'Attending'),
        ('NOT_ATTENDING', 'Not Attending'),
        ('IN_PROGRESS', 'In Progress'),
    ]
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=RSVP_CHOICES,default='IN_PROGRESS')

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return f"{self.user.email} - {self.event.title} - {self.status}"