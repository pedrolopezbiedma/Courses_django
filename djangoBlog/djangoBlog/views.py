from django.http import HttpResponse

def handle_About_Page(request):
    return HttpResponse('About page')

def handle_Home_Page(request):
    return HttpResponse('Home page')