from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User

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


def search(request):
    query = request.GET['search']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
        allpostst = Post.objects.filter(title__icontains=query)
        allpostsb = Post.objects.filter(content__icontains=query)
        allposts = allpostst.union(allpostsb)
    if allposts.count()==0:
        messages.warning(request,'No search result found please refine your search')
    params = {'allposts':allposts , 'query':query}
    return render(request,'home\\search.html',params)

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # check for correct inp
        if len(username)>10:
            messages.error(request,'Username should be less thank 10 characters')
            return redirect('home')

        if not username.isalnum():
            messages.error(request,'Username should only contain letters and numbers')
            return redirect('home')

        if pass1!=pass2:
            messages.error(request,'Your passwords does not match')
            return redirect('home')
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your iCoder has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')