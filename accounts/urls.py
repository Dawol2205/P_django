<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    path('api/', include(router.urls)),
    path('api/profile/', views.user_profile_api, name='profile_api'),
    path('api/profile/<str:username>/', views.user_profile_api, name='profile_api_user'),
    path('api/me/', views.api_user_detail),
=======
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
>>>>>>> e86b7b9f37d611aad436361104d1f4cb0dea76e7
]