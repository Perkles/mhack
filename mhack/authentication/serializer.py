from rest_framework import serializers
from authentication.models import User, Profile, Type

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['User', 'user_type', 'authentication_code', 'permissions']

class TrypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_type']