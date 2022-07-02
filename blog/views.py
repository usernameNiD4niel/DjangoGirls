from django.shortcuts import render

# Create your views here.


def post_list(request):
    context = {
        'first_name': 'Daniel Rey!'
    }
    return render(request, 'blog/index.html', context)
