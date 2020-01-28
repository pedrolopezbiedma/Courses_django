from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

def handle_Articles_List_Page(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article-list.html', { 'articles': articles })

def handle_Articles_Detail_Page(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article-detail.html', { 'article': article })

@login_required(login_url='/accounts/login/')
def handle_Articles_Create_Page(request):
    return render(request, 'articles/create-article.html')