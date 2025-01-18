from django.shortcuts import render

def home(request):
    return render(request, 'HB/index.html')
    
def about(request):
    return render(request, 'HB/about.html')


def service(request):
    return render(request, 'HB/service.html')



def product(request):
    return render(request, 'HB/product.html')






def team(request):
    return render(request, 'HB/team.html')






def testimony(request):
    return render(request, 'HB/testimonial.html')



def contact(request):
    return render(request, 'HB/contact.html')
# Create your views here.



def readmore(request):
    return render(request, 'HB/404.html')
# Create your views here.
