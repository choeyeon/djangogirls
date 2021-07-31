from rest_framework import serializers

from phone_verify.serializers import SMSVerificationSerializer




class YourUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    first_name = serializers.CharField(default="First")
    


class YourCustomSerializer(UserSerializer, SMSVerificationSerializer):
    ...