from django.shortcuts import render,HttpResponse

# Create your views here.
def bloghome(request):
    return HttpResponse('This is bloghome.We will keep all the posts here')
    
def blogpost(request,slug):
    return HttpResponse(f'This is blog :{slug}')