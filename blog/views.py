from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/posts.html', context)
# https://tutorial.djangogirls.org/en/dynamic_data_in_templates/ | Last code i wrote
