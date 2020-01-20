from rest_framework import serializers
from mpuppet.dict_handdler import extract_from
from authentication.models import User, Profile

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
        profile = Profile.objects.create(**validated_data)
        Profile.objects.create(user=profile, **user_data)
        return Profile

