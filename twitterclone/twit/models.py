from django.db import models

# Create your models here.

class twit(models.Model):
    title = models.CharField(max_length=25)
    body = models.TextField()
    twit_date = models.DateTimeField('date twitted')
    author = models.TextField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title