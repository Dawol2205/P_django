<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),  # 추가
    path('<int:pk>/delete/', views.delete, name='delete'),  # 추가
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
=======
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),  # 추가
    path('<int:pk>/delete/', views.delete, name='delete'),  # 추가
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
>>>>>>> e86b7b9f37d611aad436361104d1f4cb0dea76e7
]