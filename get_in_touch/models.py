from django.db import models


class GetInTouch(models.Model):
    name = models.CharField(max_length=250)
    info = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name
