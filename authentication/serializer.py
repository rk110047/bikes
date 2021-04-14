from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    mobile                    =   serializers.CharField(max_length=120)
    email                     =   serializers.EmailField()


class LoginSerializer(serializers.Serializer):
    mobile    =   serializers.CharField(max_length=10)