from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the DeGoshen Energy Resources</h1><p>Clean Energy, for a Cleaner Environment.</p>")

def about(request):
    return HttpResponse("<h1>This is a renouned Energy Company</h1>")

def contact(request):
    return HttpResponse("<h1>Got a question? Reach out at: degoshenresources@gmail.com </h1>")