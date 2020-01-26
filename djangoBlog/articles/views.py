from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def handle_Articles_List_Page(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles-list.html', { 'articles': articles })

def handle_Articles_Detail_Page(request, slug):
    return HttpResponse(slug)