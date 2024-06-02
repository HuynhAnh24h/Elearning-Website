
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .import user_login
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.BASE, name = 'base'),
    
    # route page 
    path('',views.HOME, name = 'home'),
    path('single_course/',views.SINGLE_COURSE, name = 'single_course'),
    path('404/',views.NOT_POUND, name='error_page'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('search',views.SEARCH_COURSE, name="search_course"),
    path('course/<slug:slug>',views.COURSE_DETAIL,name="course_detail"),
    path('contact_us/',views.CONTACT_US, name = 'contact_us'),
    path('about_us/',views.ABOUT_US, name = 'about_us'),

    # Account
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register',user_login.REGISTER, name = 'register'),
    path('doLogin', user_login.DOLOGIN, name="dologin"),
    path('accounts/profile', user_login.PROFILE, name="profile"),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name="profile_update"),
    path('my_course/',views.MY_COURSE, name="my_course"),

    # Check out
    path('checkout/<slug:slug>',views.CHECK_OUT, name="check_out")


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
