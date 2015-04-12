from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class InfoPack(models.Model):
    uuid = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name="infopack")
    flow = models.BigIntegerField()     # overall data transferred amount
    balance = models.FloatField()       # Remaining money

    def __str__(self):
        return self.user.username


class TransmitEntry(models.Model):
    user_from = models.ForeignKey(User, related_name="entries_from")     # use transmitentry_set.objects.all() to retrieve
    user_to = models.ForeignKey(User, related_name="entries_to")
    date_time = models.DateTimeField(auto_now_add=True)
    flow = models.BigIntegerField()

    @classmethod
    def create(cls, user_from, user_to, flow):
        entry = cls(user_from=user_from, user_to=user_to, flow=flow)
        return entry

    def __str__(self):
        return self.user_from.username + "-" + self.user_to.username + ":" + self.date_time.date().isoformat()
