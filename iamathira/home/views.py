from django.shortcuts import render

# Create your views here.
def home(request):
    template_path = 'home/home_index.html'
    return render(request, template_path)

def intro(request):
    template_path = "home/intro_software_testing.html"
    return render(request, template_path)