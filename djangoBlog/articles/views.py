from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def handle_Articles_List_Page(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article-list.html', { 'articles': articles })

def handle_Articles_Detail_Page(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article-detail.html', { 'article': article })

@login_required(login_url='/accounts/login/')
def handle_Articles_Create_Page(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            # Save to db
            return redirect('articleList')
        else:
            return render(request, 'articles/create-article.html', {'form': form })

    if request.method == 'GET':
        form = forms.CreateArticle()
        return render(request, 'articles/create-article.html', { 'form': form })
