from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")

        url_obj = URL.objects.create(long_url=long_url)

        return render(request, "shortener/home.html", {
            "short_code": url_obj.short_code
        })

    return render(request, "shortener/home.html")

def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    return redirect(url.long_url)