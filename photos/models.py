from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Timestamp(models.Model):
    created_time=models.DateTimeField(editable=False, default=timezone.now)
    modified=models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Picture(Timestamp):
    title=models.CharField(max_length=50, blank=True)
    url=models.URLField()
    thumb=models.URLField()

    def __str__(self):
        
        if self.title:
            return self.title
        else:
            return self.url.split('/')[-1]


class Comment(Timestamp):
    for_picture=models.ForeignKey(Picture)
    comment=models.CharField(max_length=500, blank=True)

    def __str__(self):

        return self.comment[:15]


class Story(Timestamp):
    story_title=models.CharField(max_length=20)
    story_text=models.CharField(max_length=1000)

    def __str__(self):

        return self.story_title[:15]