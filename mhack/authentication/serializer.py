from rest_framework import serializers
from authentication.models import User, Profile, ProfileType

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

class TrypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileType
        fields = ['id', 'profile_type']

class ProfileSerializer(serializers.ModelSerializer):
    user_data = UserSerlializer()
    user_type = TrypeSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user_data', 'user_type']

    def create(self, validated_data):

        user_data = validated_data.pop('user_data')
        user_type = validated_data.pop('user_type')

        print(user_type)
        profile = Profile.objects.create(**validated_data)
        print("-------------------------------------------------------------------------------------------------------------")


        Profile.objects.create(user_data=profile, **user_data)
        print("-------------------------------------------------------------------------------------------------------------")
        Profile.objects.create(user_type=profile, **user_type_data)
        print("kjahsdkjhsakjdhksahdkjh")
        return Profile

