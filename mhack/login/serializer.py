from rest_framework import serializers
from mpuppet.dict_handdler import extract_from
from .models import User, Profile

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerlializer()

    class Meta:
        model = Profile
        fields = ['user', 'profile_type']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        profile_instance = Profile.objects.create(user=user_instance, **validated_data)
        return profile_instance

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']