from rest_framework import serializers
from authentication.models import User

class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']