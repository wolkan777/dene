from django.shortcuts import render
# from .forms import PostForm


def index(request):

    return render(request, 'index.html', {
        'form': 'form',
    })
