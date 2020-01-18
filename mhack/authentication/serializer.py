from rest_framework import serializers
from authentication.models import User, Profile, Type

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

        # def create(self, validated_data):
        #     user  = User.objects.create(**validated_data)
        #     return user

class TrypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'profile_type']

        # def create(self, validated_data):
        #     type_value = Type.objects.create(**validated_data)
        #     return type_value

class ProfileSerializer(serializers.Serializer):
    user = UserSerlializer()
    user_type = TrypeSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'user_type']
    
    
    # user = UserSerlializer()
    # user_type = TrypeSerializer()
    # authentication_token = serializers.CharField(required=False)
    # avatar_url = serializers.CharField(required=False)
    # permissions = serializers.CharField(required=False)
    # timestamp = serializers.DateField(required=False)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_type_data = validated_data.pop('user_type')
        
        print(user_type_data)

        profile = Profile.objects.create(**validated_data)
    
        print(user_type_data)

        Profile.objects.create(User=profile, **user_data)
        Profile.objects.create(user_type=profile, **user_type_data)
        print("kjahsdkjhsakjdhksahdkjh")
        return Profile

