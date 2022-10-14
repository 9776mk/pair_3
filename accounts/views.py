from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
# 로그인 입력용 form
from django.contrib.auth.forms import AuthenticationForm
# 로그인 기능
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import get_user_model


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        # AuthenticationFrom은 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 form에서 인증된 유저 정보를 가져옴
            auth_login(request, form.get_user())
            ######## 다른 곳으로 보내줄 곳을 위해 수정할 것! #######
            return redirect('accounts:index')

    else:
         form = AuthenticationForm()
    context = {
        'form' : form
    }
    ######## 다른 곳으로 보내줄 곳을 위해 수정할 것! #######
    return render(request, 'accounts/login.html', context)

def index(request):
    user = get_user_model().objects.all()
    context = {
        'user_': user
    }
    return render(request, "accounts/index.html", context)

def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context ={
        'user_' : user
    }
    return render(request,"accounts/detail.html",context)

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
    'form': form,
    }
    return render(request, 'accounts/update.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')