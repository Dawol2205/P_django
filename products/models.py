from django.db import models
from django.conf import settings
import re

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        # 특수문자와 공백 제거
        self.name = re.sub(r'[^\w\s]', '', self.name)
        self.name = self.name.replace(' ', '')
        super().clean()

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_products')
    hashtags = models.ManyToManyField(Hashtag, related_name='products')
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title