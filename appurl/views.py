from django.shortcuts import render
from django.shortcuts import redirect
from hashids import Hashids
from django.views.generic import View, CreateView, ListView, TemplateView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from appurl.models import Bookmark
hashids = Hashids()

# Create your views here.


class ViewIndex(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


class ViewBookmark(TemplateView):
    template_name = "bookmarks.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['bookmark'] = Bookmark.objects.filter(user=user)
        return context


class AddBookmark(CreateView):
    model = Bookmark
    fields = ['title', 'link', 'description']
    success_url = '/'

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        hashstring = Hashids(salt=bookmark.link)
        linkhash = hashstring.encode(123456789)
        bookmark.shortlink = linkhash
        bookmark.user = self.request.user
        return super(AddBookmark, self).form_valid(form)


class UpdateBookmark(UpdateView):
    model = Bookmark
    fields = ['title', 'link', 'description']
    template_name = 'updatebookmark.html'
    success_url = '/'


class ViewProfile(TemplateView):
    template_name = "profiletemp.html"


class BookmarkInfo(TemplateView):
    template_name = 'bookmarkinfo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shortlink = self.kwargs.get('shortlink', None)
        context['bookmark'] = Bookmark.objects.get(shortlink=shortlink)
        unhash = hashids.decode(shortlink)
        print(unhash)
        # return HttpResponseRedirect('http://www.google.com')
        return context

    # def get(self, args, **kwargs):
    #    return HttpResponseRedirect('www.google.com')

    """
    template_name = "bookmarkinfo.html"

    permanent = False
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        shortlink = self.kwargs.get('shortlink', None)
        context['bookmark'] = Bookmark.objects.get(shortlink=shortlink)
        bookmark = Bookmark.objects.get(shortlink=shortlink)
        return redirect('www.google.com')
    # def get_redirect_view(self, request, args, **kwargs):
        # context = super().get_context_data(**kwargs)
        # shortlink = self.kwargs.get('shortlink', None)
        # bookmarkinfo = Bookmark.objects.get(shortlink=shortlink)
        # dehash = hashids.decode(shortlink)
        # url = deshaed url
        # redirect_to = dehash
        # return(redirect_to)
        """
