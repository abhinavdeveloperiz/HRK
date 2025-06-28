from django.shortcuts import render
from app.models import student_gallery, office_gallery,Service,Head,Testimonial

# Create your views here.
def Home(request):
    student= student_gallery.objects.all()
    office = office_gallery.objects.all()
    service= Service.objects.all()
    head_image = Head.objects.first()
    testimonials= Testimonial.objects.all() 
    context={
        'student': student,
        'office': office,
        'service': service,
        "image":head_image,
        'testimonials': testimonials
    }
    return render(request, 'home.html',context)

def About(request):
    return render(request, 'about.html')

def Services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html',context)

def Service_details(request,id):
    service=Service.objects.get(id=id)
    context = {
        'service': service
    }
    return render(request, 'service_details.html',context)

from django.core.paginator import Paginator

def Student_gallery(request):
    office = student_gallery.objects.all()
    paginator = Paginator(office, 10)  # Show 8 images per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'student_gallery.html', {'page_obj': page_obj})



def Office_gallery(request):

    office = office_gallery.objects.all()
    paginator = Paginator(office, 10)  # Show 8 images per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'office_gallery.html', {'page_obj': page_obj})



def Contact(request):   
    return render(request, 'contact.html')