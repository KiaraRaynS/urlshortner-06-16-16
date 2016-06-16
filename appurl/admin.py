from django.contrib import admin
from appurl.models import Bookmark, Profile

# Register your models here.

admin.site.register([Bookmark, Profile])
