from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    short_url = None

    if request.method == "POST":
        long_url = request.POST.get("long_url")

        url_obj = URL.objects.create(long_url=long_url)

        short_url = request.build_absolute_uri("/") + url_obj.short_code

    return render(request,"shortener/home.html",{
        "short_url": short_url
    })

def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    url.clicks += 1
    url.save()
    return redirect(url.long_url)