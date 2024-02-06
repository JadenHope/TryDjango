from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_list(request):
    query_set       = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        query_set = (query_set | my_qs).distinct()
    template_name   = "blog/list.html"
    context         = {"object_list": query_set}

    return render(request, template_name, context)


@staff_member_required
def blog_post_create(request):
    form = BlogPostModelForm(
        request.POST or None,
        request.FILES or None,
    )
    if form.is_valid():
        obj         = form.save(commit=False)
        obj.user    = request.user
        obj.save()
        form        = BlogPostModelForm()

    template_name   = "form.html"
    context         = {"form": form}

    return render(request, template_name, context)


def blog_post_retrieve(request, slug):
    template_name   = "blog/retrieve.html"
    obj             = get_object_or_404(BlogPost, slug=slug)
    context         = {"object": obj}

    return render(request, template_name, context)


@staff_member_required
def blog_post_update(request, slug):
    template_name   = "form.html"
    obj             = get_object_or_404(BlogPost, slug=slug)
    form            = BlogPostModelForm(
        request.POST or None,
        request.FILES or None,
        instance=obj
    )
    if form.is_valid():
        form.save()

    context = {
        "form"      : form,
        "title"     : f"Update {obj.title}",
    }

    return render(request, template_name, context)


@staff_member_required
def blog_post_delete(request, slug):
    template_name   = "blog/delete.html"
    obj             = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST":
        obj.delete()
        return redirect("/blog")

    context = {
        "object"    : obj,
        "form"      : None
    }

    return render(request, template_name, context)
