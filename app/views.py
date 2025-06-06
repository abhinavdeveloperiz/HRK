from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'services.html')

def Student_gallery(request):
    return render(request, 'student_gallery.html')

def Office_gallery(request):
    return render(request, 'office_gallery.html')

def Contact(request):   
    return render(request, 'contact.html')