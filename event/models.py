from django.db import models
from django.contrib.auth.models import User


class calender(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)

class events(models.Model):
    users = models.ManyToManyField(calender)
    message = models.CharField(max_length=200)
    event_start = models.DateTimeField()
    event_end  = models.DateTimeField()