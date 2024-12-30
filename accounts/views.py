<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileUpdateForm
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('products:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, '로그인 되었습니다.')
            return redirect('products:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('products:index')

@login_required
def profile(request, username=None):
    User = get_user_model()
    # username이 주어지지 않은 경우 현재 로그인한 사용자의 프로필
    if username is None:
        profile_user = request.user
    else:
        profile_user = get_object_or_404(User, username=username)
    
    if request.method == 'POST' and request.user == profile_user:
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 업데이트되었습니다.')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=profile_user)
    
    context = {
        'profile_user': profile_user,
        'form': form,
        'user_products': profile_user.product_set.all(),
        'liked_products': profile_user.liked_products.all(),
        'user_posts': profile_user.post_set.all(),
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    if request.method == 'POST':
        User = get_user_model()
        you = get_object_or_404(User, pk=user_pk)
        me = request.user

        if you != me:
            if me in you.followers.all():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_api(request, username=None):
    User = get_user_model()
    if username is None:
        user = request.user
    else:
        user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def api_user_detail(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileUpdateForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('products:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, '로그인 되었습니다.')
            return redirect('products:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('products:index')

@login_required
def profile(request, username=None):
    User = get_user_model()
    # username이 주어지지 않은 경우 현재 로그인한 사용자의 프로필
    if username is None:
        profile_user = request.user
    else:
        profile_user = get_object_or_404(User, username=username)
    
    if request.method == 'POST' and request.user == profile_user:
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 업데이트되었습니다.')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=profile_user)
    
    context = {
        'profile_user': profile_user,
        'form': form,
        'user_products': profile_user.product_set.all(),
        'liked_products': profile_user.liked_products.all(),
        'user_posts': profile_user.post_set.all(),
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    if request.method == 'POST':
        User = get_user_model()
        you = get_object_or_404(User, pk=user_pk)
        me = request.user

        if you != me:
            if me in you.followers.all():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
    return JsonResponse({'error': 'Invalid request'}, status=400)
>>>>>>> e86b7b9f37d611aad436361104d1f4cb0dea76e7
