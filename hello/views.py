from django.shortcuts import render, HttpResponse  #render is used to render the template

# Create your views here.
def index(request):
    return render (request,'first.html')


    #return HttpResponse("This is the home page.")

def about(request):
    return HttpResponse("This is the about page")

def location(request):
    return HttpResponse("This is the location of the Aafrin Design.")

