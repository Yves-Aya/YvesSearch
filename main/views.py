from django.shortcuts import render
from . models import  post
from django.db.models import Q
from django.contrib import  messages
from django.http import *
from .forms import  postForm
from .models import post

def home(request):
    if request.method == "POST":
        srch = request.POST['search']

        if srch:
            match = post.objects.filter(Q(name__icontains=srch)| Q(name__startswith=srch)|Q(name__endswith=srch))

            if match:
                return render(request,'main/home.html',{'infos':match})

            else:
                messages.error(request,'sorry your document has not yet been uploaded in our system ! please be patient it will soon be uploaded')
        else:
            return HttpResponseRedirect('main-home')


    return render(request,'main/home.html')


def post_create(request):
    form = postForm(request.POST or None,request.FILES or None)

    if form.is_valid():
       form.save()
       return HttpResponseRedirect('')

    context = {
     "form":form,
    }
    return render(request,'main/addpost.html',context)
