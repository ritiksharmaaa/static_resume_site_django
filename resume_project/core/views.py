from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home_page(request):
    context={
        "home" :"active"
    }
    return render(request ,"core/home.html" ,context )
    # return HttpResponse("app is running ")
   
def contact_page(request):
    context={
        "contact": "active"
    }
    return render(request, "core/contact.html",  context)

