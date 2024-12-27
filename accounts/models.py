from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    # 기본 프로필 이미지 설정
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    # 팔로우 기능을 위한 ManyToMany 필드
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    def __str__(self):
        return self.username