# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortenedURL

def home(request):
    return render(request, 'home.html')

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url.startswith('https://www.youtube.com/'):
            shortened_url = ShortenedURL(original_url=original_url)
            shortened_url.save()
            return render(request, 'shorten_url.html', {'shortened_url': shortened_url})
        else:
            return HttpResponse("Invalid URL. Please provide a YouTube URL starting with 'https://www.youtube.com/'.")
    return redirect('home')

def redirect_url(request, short_url):
    shortened_url = ShortenedURL.objects.get(short_url=short_url)
    return redirect(shortened_url.original_url)
