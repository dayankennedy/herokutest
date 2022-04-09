from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'heroku/home.html')


# This is the index page
def base(request):
    return render(request, 'heroku/base.html')



# This the index page
def index(request):
    return render(request, 'heroku/index.html')
