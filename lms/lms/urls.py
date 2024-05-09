
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
    path('contact_us/',views.CONTACT_US, name = 'contact_us'),
    path('about_us/',views.ABOUT_US, name = 'about_us'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register',user_login.REGISTER, name = 'register'),
    path('doLogin', user_login.DOLOGIN, name="dologin"),
    path('accounts/profile', user_login.PROFILE, name="profile"),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name="profile_update"),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
