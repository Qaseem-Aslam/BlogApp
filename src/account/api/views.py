from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
	if request.method == 'POST':
		serializers = RegistrationSerializer(data=request.data)
		data={}
		if serializers.is_valid():
			account = serializers.save()
			data['success'] = "Registration successful!"
			data['email'] = account.email
			data['username'] = account.username
		else:
			data = serializers.errors
		return Response(data)