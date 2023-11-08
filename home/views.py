from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "home/index.html", {'post': posts})


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post_detail = Post.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'home/post_detail.html', {'details': post_detail})


class PostDeleteView(LoginRequiredMixin, View):
    def get (self, request, post_id):
        post_delete = Post.objects.get(id=post_id)
        if post_delete.user.id == request.user.id:
            post_delete.delete()
            messages.success(request, 'this post was deleted', 'success')
        else:
            messages.error(request, "you can not delete this post", 'danger')
        return redirect('home:home')

