from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    
    class Meta:
        model = get_user_model()
        fields = (
            'id', 
            'username', 
            'profile_image', 
            'following_count', 
            'followers_count',
            'email',
        )
        read_only_fields = ('username',)

    def get_following_count(self, obj):
        return obj.followings.count()

    def get_followers_count(self, obj):
        return obj.followers.count()
