from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Avg
from .models import Post
# Create your views here.


def post_list(request):

    posts = Post.objects.all().annotate(comment_count=Count("id"))
    avg_views = Post.objects.aggregate(Avg("views"))


    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, "blog/post_list.html", {"page_obj": page_obj, "avg_views": avg_views})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views +=1
    post.save()
    return render(request, "blog/post_detail.html", {"post": post})

