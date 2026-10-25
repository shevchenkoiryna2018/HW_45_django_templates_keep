from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'keep/index.html', context)


def demo(request):
    context = {}
    return render(request, 'keep/demo.html', context)


def archives(request):
    context = {}
    return render(request, 'keep/archives.html', context)


def blog(request):
    context = {}
    return render(request, 'keep/blog.html', context)


def blog_single(request):
    context = {}
    return render(request, 'keep/single.html', context)


def page(request):
    context = {}
    return render(request, 'keep/page.html', context)
