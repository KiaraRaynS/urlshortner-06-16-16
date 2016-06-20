"""urlshortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appurl.views import SignUpView, ViewBookmark, AddBookmark, ViewProfile, UpdateBookmark, DeleteBookmark, AddViewCount, ViewIndex
from django.contrib.auth.views import logout, login
# ViewIndex

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewIndex.as_view(), name='index'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^yourbookmarks/(?P<pk>\w+)/$', ViewBookmark.as_view(), name='viewbookmarks'),
    url(r'^makebookmark/$', AddBookmark.as_view(), name='addbookmark'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^accounts/profile/$', ViewProfile.as_view(), name='profile'),
    url(r'^(?P<shortlink>\w+)/$', AddViewCount.as_view(), name='redirect'),
    url(r'^update/(?P<pk>\w+)/$', UpdateBookmark.as_view(), name='update'),
    url(r'^delete/(?P<pk>\w+)/$', DeleteBookmark.as_view(), name='delete'),
]
