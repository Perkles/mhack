from rest_framework import serializers
from authentication.models import User, Profile, ProfileType

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class TrypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileType
        fields = ['profile_type']

class ProfileSerializer(serializers.Serializer):
    user = UserSerlializer()
    user_type = TrypeSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'user_type']
    

    def create(self, validated_data):
        print(validated_data)


        profile = Profile.objects.create(**validated_data)
        user_data = validated_data.pop('user')
        print(validated_data)
        user_type_data = validated_data.pop('user_type')
        
        print(validated_data)
        print(profile)

        Profile.objects.create(User=profile, **user_data)
        print("-------------------------------------------------------------------------------------------------------------")
        Profile.objects.create(user_type=profile, **user_type_data)
        print("kjahsdkjhsakjdhksahdkjh")
        return Profile

