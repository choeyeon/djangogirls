from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

#from phone_verify.api import VerificationViewSet
#from phone.verify import serializers as phone_serializers


#from . import services, serializers


#class YourCustomViewSet(VerificationViewSet):
#   def verify_and_register(self, request):
#        
#
#        serializer = phone_serializers.SMSVerificationSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
# 
#
#        serializer = serializers.YourUserSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        user = services.create_user_account(**serializer.validated_data)
#
#        return Response(serializer.data)