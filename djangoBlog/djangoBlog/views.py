from django.shortcuts import render, redirect

def handle_Home_Page(request):
    return redirect('articleList')


def handle_About_Page(request):
    #return HttpResponse('About page')
    return render(request, 'about.html')
