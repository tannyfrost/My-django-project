from django.shortcuts import redirect, render
from website.forms import contactForm
from website.models import indexContent

# Create your views here.

def home(request):
    sliderText = indexContent()
    return render(request, 'temp/index.html',{'slider':sliderText})
def index(request):
    return redirect('home')
def about(request):
    return render(request, 'temp/about.html')
def services(request):
    return render(request, 'temp/services.html')
def portfolio(request):
    return render(request, 'temp/portfolio.html')
def testimonials(request):
    return render(request, 'temp/testimonials.html')
def blog(request):
    return render(request, 'temp/blog.html')
def contact(request):
    contact = contactForm(request.POST or None, request.FILES or None)

    if contact.is_valid():
        contact.save()
        return render(request, 'temp/index.html')
    return render(request, 'temp/contact.html',{'form':contact})
