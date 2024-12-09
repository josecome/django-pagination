from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Post
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj })

    