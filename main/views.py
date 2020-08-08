from django.shortcuts import render
from .models import recognition, enquiry
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
#from .forms import RegisterForm
#from django.core.mail import send_mail

# Create your views here.

def homepage(request):
#    return render(request=request,
#    template_name='main/home.html',
#    context={"recognition": recognition.objects.all}
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('parent_name') and request.POST.get('student_name') and request.POST.get('email') and request.POST.get('phone'):
            submitform=enquiry()
            submitform.parent_name=request.POST.get('parent_name')
            submitform.student_name=request.POST.get('student_name')
            submitform.email=request.POST.get('email')
            submitform.phone=request.POST.get('phone')
            submitform.age=request.POST.get('age')
            submitform.reasons=request.POST.get('reasons')
            submitform.save()
            messages.success(request, f"Thanks for reaching out, we will get in touch with you shortly!")
            #return redirect("main:homepage")
            return render(request=request,
            template_name='main/home.html',
             context={"recognition": recognition.objects.all})

    else:
        return render(request=request,template_name='main/home.html',context={"recognition": recognition.objects.all})

#def register(request):
#    if response.method == "POST":
#        print(response.POST)
#        if response.POST.get("enquiry"):



#def register(request):
#    if request.method == 'POST':
#        print(request.POST)
#        if request.POST.get('parent_name') and request.POST.get('student_name') and request.POST.get('email') and request.POST.get('phone'):
#            submitform=enquiry()
#            submitform.parent_name=request.POST.get('parent_name')
#            submitform.student_name=request.POST.get('student_name')
#            submitform.email=request.POST.get('email')
##            submitform.age=request.POST.get('age')
#            submitform.reasons=request.POST.get('reasons')
#            submitform.save()
#            messages.success(request, f"Thanks for reaching out, we will get in touch with you shortly!")
            #return redirect("main:homepage")
#            return render(request, 'main/home.html')
#    else:
#        return render(request, 'main/home.html')
