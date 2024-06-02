
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse
from app.models import Categories
from app.models import Course
from app.models import Level
from app.models import Video
from app.models import UserCourse
from django.db.models import Sum

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

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    if category:
        course = Course.objects.filter(category__id__in = category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course': course
    }
    t = render_to_string('ajax/course.html',context)

    return JsonResponse({'data': t})

def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query )
    context = {
        'course': course
    }
    return render(request,'search/search.html',context)

def COURSE_DETAIL(request,slug):
    course = Course.objects.filter(slug = slug)
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum=Sum('time_duration'))

    course_id = Course.objects.get(slug = slug)
    # Xử lý cho khoá học free
    try:
        check_enroll = UserCourse.objects.get( user = request.user, course = course_id)
    except UserCourse.DoesNotExist:
        check_enroll = None

    if course.exists():
        course = course.first
    else:
        return redirect('404/')
    
    context = {
        'course': course,
        'time_duration':time_duration,
        'check_enroll':check_enroll
    }
    return render(request, 'course_detail/course_detail.html',context)

# Mua khoá học online 
def CHECK_OUT(request,slug):
    course = Course.objects.get(slug = slug)

    # Xử lý cho khoá học free
    if course.price == 0:
        course = UserCourse(
            user = request.user,
            course = course
        )
        course.save()
        messages.success(request,'Khoá học đã được thêm ')
        return redirect('my_course')
    return render(request,'checkout/check_out.html')

# Danh sách khoá học của user
def MY_COURSE(request):
    course = UserCourse.objects.filter(user = request.user)

    context = {
        'course' : course,
    }
    return render(request,'my-course/my-course.html',context)

def NOT_POUND(request):
    return render(request,'404/error_page.html')

def CONTACT_US(request):
    return render(request,'main/contact_us.html')


def ABOUT_US(request):
    return render(request,'main/about_us.html')


