from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from app.EmailBackend import EmailBackend
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def base_view(request):
    return render(request, 'base.html')

def login_veiw(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type=='1':
            return redirect('hod_home')
        elif user.user_type=='2':
            return redirect('student_home')
        else:
            return redirect('staff_home')
    else:
        return render(request, 'login.html')

def dologin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request, username=email, password=password)
        
        if user!=None:
            login(request, user)
            user_type = user.user_type
            
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('student_home')
            elif user_type == '3':
                return redirect('staff_home')
            elif user_type == '4':
                return redirect('transport_home')
            else:
                messages.error(request, "Wrong Email or Password")
                return redirect('login')
        messages.error(request, "Wrong Email or Password")
        return redirect('login')
        

def dologout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def profile_view(request):
    staff = None
    student = None
    user = None
    try:
        
        user = CustomUser.objects.get(id=request.user.id)
        
        if user.user_type == '1':
            pass
        elif user.user_type == '2':
            student = Student.objects.get(admin=request.user)
        elif user.user_type == '3':
            staff = Staff.objects.get(admin=request.user)
    except Exception as e:
        print(e)
    return render(request, 'view_profile.html', {'user': user, 'student': student, 'staff': staff})

@login_required(login_url='/')
def profile(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
    except Exception as e:
        print(e)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)
    
@login_required(login_url='/')
def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        try:
            customize_user = CustomUser.objects.get(admin=request.user)
            customize_user.first_name =first_name
            customize_user.last_name = last_name
            if password != None and password != '':
                customize_user.set_password(password)
            if profile_pic!= None and profile_pic != '':
                customize_user.profile_pic = profile_pic          
            customize_user.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
        except Exception as e:
            print(e)
    return render(request, 'profile.html')

def registration(request):
    return render(request, 'registration.html')

def check_registration(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        customuser = CustomUser()
        
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.email = email
        customuser.username = username
        customuser.user_type = 4        
        if profile_pic!= None and profile_pic != '':
            customuser.profile_pic = profile_pic
        if password==confirm_password:
            customuser.set_password(password)
        else:
            messages.error(request, "Password and confirm password are not same!")
        customuser.save()
        messages.success(request, "User create successfully")
        return redirect('login')