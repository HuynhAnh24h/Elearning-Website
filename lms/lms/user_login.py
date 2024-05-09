from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.emailBackend import EmailBackEnd
def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check email
        if User.objects.filter(email = email).exists():
           messages.warning(request, "Email đã tồn tại")
           return redirect('register')

        # check username
        if User.objects.filter(username = username).exists():
           messages.warning(request, "Tên người dùng đã tổn tại")
           return redirect('register')
        
        user = User(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request,'registration/register.html')

def DOLOGIN(request):
  if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
		
        user = EmailBackEnd.authenticate(request,
                                     username=email,
                                     password=password)
        if user!=None:
           login(request,user)
           return redirect('home')
        else:
           messages.error(request,'Tài khoản mật khẩu không chính xác')
           return redirect('login')
  
def PROFILE(request):
    return render(request,'registration/profile.html')

def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Cập nhật profile thành công. ')
        return redirect('profile')