from hashids import Hashids

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, ListView, TemplateView, RedirectView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appurl.models import Bookmark, ViewCount

import datetime

hashids = Hashids()

# Create your views here.


class ViewIndex(ListView):
    template_name = 'index.html'
    model = Bookmark
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookmark = Bookmark.objects.all()
        context['bookmark'] = bookmark
        return context


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


class ViewProfile(TemplateView):
    template_name = "profiletemp.html"


class ViewBookmark(TemplateView):
    template_name = "bookmarks.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['bookmark'] = Bookmark.objects.filter(user=user)
        return context


# Bookmark related Classes


class AddBookmark(CreateView):
    model = Bookmark
    fields = ['title', 'link', 'description', 'public']
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
    fields = ['title', 'link', 'description', 'public']
    template_name = 'updatebookmark.html'
    success_url = '/'


class DeleteBookmark(DeleteView):
    model = Bookmark
    success_url = '/'
    template_name = 'deletebookmark.html'


class AddViewCount(RedirectView):
    template_name = 'bookmarkinfo.html'

    def get(self, request, *args,  **kwargs):
        shortlink = self.kwargs.get('shortlink', None)
        bookmark = Bookmark.objects.get(shortlink=shortlink)
        self.url = bookmark.link
        bookmark.view += 1
        bookmark.save()
        ViewCount.objects.create(bookmark=bookmark, date=datetime.datetime.now())
        return super(AddViewCount, self).get(request, *args, **kwargs)

# class BookmarkInfo(TemplateView):
#    template_name = 'bookmarkinfo.html'


# class PastEntryList(ListView):
