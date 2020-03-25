from django.shortcuts import render,HttpResponse
from blog.models import Post        
# Create your views here.
def bloghome(request):
    allposts = Post.objects.all()
    print(allposts)
    context = {'allposts':allposts}
    return render(request,'blog\\bloghome.html',context)
    #return HttpResponse('This is bloghome.We will keep all the posts here')
    
def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog\\blogpost.html',context)
    #return HttpResponse(f'This is blog :{slug}')