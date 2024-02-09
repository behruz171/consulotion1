from django.shortcuts import render
from .models import *
def index(request):
    baner = Baner.objects.all()
    static = Static.objects.first()
    services = Service.objects.all()
    review = Review.objects.all()
    result = Result.objects.all()

    context = {
        "baner": baner,
        "static": static,
        "services": services,
        "review": review,
        "result": result
    }

    if request.method == 'POST':
        first_name =request.POST.get('first_name')
        last_name =  request.POST.get('last_name')
        choise = request.POST.get('choise')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            choise_insitution = choise,
            phone = phone,
            message=message
        )

    return render(request, 'index.html', context)

def about(request):
    static = Static.objects.first()
    result = Result.objects.all()
    context = {
        "static": static,
        "result": result
    }
    return render(request, 'about.html', context)

def project(request):
    
    review = Review.objects.all()

    context = {
        "review": review,
    }
    return render(request, 'project.html', context)

def services(request):
    services = Service.objects.all()


    context = {
        "services": services,
    }
    return render(request, 'services.html', context)

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
