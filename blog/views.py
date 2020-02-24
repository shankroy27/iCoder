from django.shortcuts import render,HttpResponse

# Create your views here.
def bloghome(request):
    return render(request,'blog\\bloghome.html')
    #return HttpResponse('This is bloghome.We will keep all the posts here')
    
def blogpost(request,slug):
    return render(request,'blog\\blogpost.html')
    #return HttpResponse(f'This is blog :{slug}')