from django.shortcuts import render

# Create your views here.


def handle_Articles_List_Page(request):
    return render(request, 'articles/articles-list.html')
