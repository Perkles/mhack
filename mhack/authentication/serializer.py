from rest_framework import serializers
from authentication.models import User, Profile, Type

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerlializer()
    user_type = serializers.IntegerField()
    authentication_token = serializers.CharField()
    avatar_url = serializers.CharField()
    permissions = serializers.CharField()
    timestamp = serializers.DateField()

class TrypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_type']