from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls.base import reverse_lazy
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

                     

def logout_user(request):
    logout(request)
    return redirect('accounts/index')

def index(request):
    form = None
    if request.method == 'POST':
        print("POST request received:", request.POST)  # 打印 POST 数据

        # 处理登录
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!", extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('polls:list')  # 登录成功后跳转到首页
            else:
                messages.error(request, "Username or password is not correct", extra_tags='alert alert-warning alert-dismissible fade show')

        # 处理注册
        else:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                print("Form is valid!")
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                email = form.cleaned_data['email']

                check1 = False
                check2 = False
                check3 = False

                # 检查密码是否匹配
                if password1 != password2:
                    check1 = True
                    messages.error(request, "Passwords do not match!", extra_tags='alert alert-warning alert-dismissible fade show')

                # 检查邮箱是否已存在
                if User.objects.filter(email=email).exists():
                    check2 = True
                    messages.error(request, "Email already exists!", extra_tags='alert alert-warning alert-dismissible fade show')

                # 检查用户名是否已存在
                if User.objects.filter(username=username).exists():
                    check3 = True
                    messages.error(request, "Username already exists!", extra_tags='alert alert-warning alert-dismissible fade show')

                # 如果有任何错误，停留在当前页面并显示错误信息
                if check1 or check2 or check3:
                    messages.error(request, "Registration failed. Please correct the errors.", extra_tags='alert alert-warning alert-dismissible fade show')
                else:
                    print("Registering and logging in user...")
                    # 创建用户并自动登录
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.save()
                    user = authenticate(request, username=username, password=password1)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Thanks for registering, you are now logged in!", extra_tags='alert alert-success alert-dismissible fade show')
                        return redirect('polls:list')  # 注册并登录后跳转到首页
                    else:
                        messages.error(request, "Authentication failed. Please try again.", extra_tags='alert alert-warning alert-dismissible fade show')
            else:
                print("Form is not valid.")
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"Error in {field}: {error}")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/index.html', {'form': form})