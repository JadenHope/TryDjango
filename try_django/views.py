from django.shortcuts   import render
from .forms             import ContactForm
from blog.models        import BlogPost


def home_page(request):
    context = {"title": "Home"}
    qs = BlogPost.objects.all()[:5]
    context["list"] = qs

    return render(request, "home.html", context)


def about_page(request):
    context = {"title": "About"}
    return render(request, "about.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()

    context = {
        "title":    "Contact Us",
        "form":     form
    }
    return render(request, "form.html", context)
