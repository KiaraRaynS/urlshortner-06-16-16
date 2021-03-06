from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    link = models.TextField()
    shortlink = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # make a foreignkey
    user = models.ForeignKey(User)
    view = models.IntegerField(default=0)
    public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # This is uneeded
    # bookmarks = models.ManyToManyField('appurl.Bookmark')


class ViewCount(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bookmark = models.ForeignKey(Bookmark)
