from rest_framework import serializers
from .models import User, Profile, FavoriteProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'description']

class FavoriteProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = FavoriteProfile
        fields = ['id', 'profile']

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True) 
    profiles = ProfileSerializer(many=True, read_only=True)
    favorite_profiles = FavoriteProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'profiles', 'favorite_profiles']
