from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filter import CategoryFilter
from django.contrib import messages


# Create your views here.
def loginPage(request):
    return render(request,'design/login.html')
def home(request):
    return render(request,'design/homepage.html')

def gallery(request):

    category = request.GET.get('category')
    if category == None:
        photos = photo.objects.all()
    else:
        photos = photo.objects.filter(category__name__contains=category)
    

    categories = Category.objects.all() 
    myfilter = CategoryFilter(request.GET, queryset=categories)
    categories = myfilter.qs
    context = {'categories':categories, 'photos':photos, 'myfilter':myfilter}
    return render(request,'design/gallery.html',context)

def viewPhoto(request, pk):
    Photo = photo.objects.get(id=pk)
    return render(request, 'design/photo.html' , {'photo':Photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
    
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        Photo = photo.objects.create(
            category = category,
            description = data['description'],
            image = image
        )

        return redirect('gallery')


    context = {'categories':categories}
    return render(request, 'design/add.html',context)