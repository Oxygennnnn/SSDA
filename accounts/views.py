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
    if request.method == 'POST':
        print("POST request received:", request.POST)  # 打印 POST 数据
        # 处理登录
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('polls:list')  # 登录成功后跳转到首页
            else:
                messages.error(request, "Username or password is not correct", extra_tags='alert alert-warning alert-dismissible fade show')
        
        # 处理注册
        else:
            check1 = False
            check2 = False
            check3 = False

            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                print("Form is valid!")
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                email = form.cleaned_data['email']

                # 检查密码是否匹配
                if password1 != password2:
                    print('Passwords do not match!')
                    check1 = True
                    messages.error(request, 'Password doesn\'t match!',
                                    extra_tags='alert alert-warning alert-dismissible fade show')

                # 检查邮箱是否已存在
                if User.objects.filter(email=email).exists():
                    print('Email already exists!')
                    check2 = True
                    messages.error(request, 'Email already exists!',
                                    extra_tags='alert alert-warning alert-dismissible fade show')

                # 检查用户名是否已存在
                if User.objects.filter(username=username).exists():
                    print('Username already exists!')
                    check3 = True
                    messages.error(request, 'Username already exists!',
                                    extra_tags='alert alert-warning alert-dismissible fade show')

                # 如果有错误，返回错误信息
                if check1 or check2 or check3:
                    print('Check failed!')
                    messages.error(request, 'Registration failed!',
                                   extra_tags='alert alert-warning alert-dismissible fade show')
                else:
                    print('log in')
                    # 创建用户并自动登录
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    # 使用 authenticate 和 login 来自动登录
                    user = authenticate(request, username=username, password=password1)
                    if user is not None:
                        login(request, user)
                        print(f"Logged in user: {request.user}") 
                        messages.success(request, 'Thanks for registering and you are now logged in!',
                                         extra_tags='alert alert-success alert-dismissible fade show')
                        print("Redirecting to polls list")
                        return redirect('polls:list')  # 注册并登录后跳转到首页
                    else:
                        messages.error(request, 'Authentication failed. Please try again.',extra_tags='alert alert-warning alert-dismissible fade show')
            else:
                print("Form is not valid.")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/index.html', {'form': form})



    