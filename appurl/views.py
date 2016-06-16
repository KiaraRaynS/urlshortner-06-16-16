from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from appurl.models import Bookmark
from django.contrib.auth.decorators import login_required

# Create your views here.


class ViewIndex(View):

    def get(self, request):
        return HttpResponse("Hello, world!")


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


@login_required
class ViewBookmarks(ListView):
    model = User


class AddBookmark(CreateView):
    model = Bookmark
    fields = ['title', 'link', 'description']
