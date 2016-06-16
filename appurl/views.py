from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.


class ViewIndex(View):

    def get(self, request):
        return HttpResponse("Hello, world!")


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'
