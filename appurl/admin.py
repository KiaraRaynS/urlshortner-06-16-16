from django.contrib import admin
from appurl.models import Bookmark, Profile, ViewCount

# Register your models here.

admin.site.register([Bookmark, Profile, ViewCount])
