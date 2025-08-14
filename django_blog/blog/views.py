from django.shortcuts import render
from django.views import View

class BasePreview(View):
    def get(self, request):
        return render(request, "blog/home.html")

class PostListView(View):
    def get(self, request):
        return render(request, "blog/post_list.html")
