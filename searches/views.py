from django.shortcuts import render, redirect

from blog.models import BlogPost

from .models import SearchQuery


# Create your views here.
def search_view(request):
    query       = request.GET.get('q', None)
    user        = None
    context     = {"query": query}

    if request.user.is_authenticated:
        user = request.user

    if not query:
        return redirect('/')
    else:
        SearchQuery.objects.create(query=query, user=user)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list

    return render(request, 'searches/view.html', context)
