from django.db import models
from django.utils import timezone

class Discovery(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=220)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def publishDiscovery(self):
        self.save()

    def __str__(self):
        return self.title
