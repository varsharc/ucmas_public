from django.shortcuts import render
from .models import section

# Create your views here.

def homepage(request):
    return render(request=request,
    template_name='main/home.html',
    context={"sections": section.objects.all})
