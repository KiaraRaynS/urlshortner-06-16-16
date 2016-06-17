from django.shortcuts import render
from hashids import Hashids
from django.views.generic import View, CreateView, ListView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from appurl.models import Bookmark
from django.contrib.auth.decorators import login_required
hashids = Hashids()

# Create your views here.


class ViewIndex(View):

    def get(self, request):
        return HttpResponse("Hello, world!", "Print")


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


@login_required
class ViewBookmarks(TemplateView):
    template_name = "bookmarks.html"


class AddBookmark(CreateView):
    model = Bookmark
    fields = ['title', 'link', 'description']
    success_url = '/'

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        hashstring = Hashids(salt=bookmark.link)
        linkhash = hashstring.encode(123)
        bookmark.shortlink = linkhash
        bookmark.user = self.request.user
        return super(AddBookmark, self).form_valid(form)


class ViewProfile(TemplateView):
    template_name = "profiletemp.html"
