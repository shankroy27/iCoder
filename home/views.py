from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home\home.html')
    
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(msg)<4:
            messages.error(request, 'Please fill the from correctly')
        else:
            c = Contact(name=name,email=email,phone=phone,content=msg)
            c.save()
            messages.success(request, 'Your message has been sent successfully')
    return render(request,'home\contact.html')

def about(request):
    messages.error(request, 'Welcome to contact1')
    messages.error(request, 'Welcome to contact2')
    messages.error(request, 'Welcome to contact2')
    return render(request,'home\\about.html')