from django.shortcuts import redirect, render
from app.models import Categories
from app.models import Course
from app.models import Level

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    print(course)
    context = {
        'category':category,
        'course':course,
    }
    return render(request,'main/home.html',context)

def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all().order_by('id')[0:5]
    course = Course.objects.all().order_by('id')[0:5]
    context = {
        'category':category,
        'level': level,
        'course': course
    }
    return render(request,'main/single_course.html', context)

def CONTACT_US(request):
    return render(request,'main/contact_us.html')

def ABOUT_US(request):
    return render(request,'main/about_us.html')


