from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import User
import jwt
key = 'varun123'

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    user = User.objects.filter(username=username, email=email).first()
    if user is not None:
        token = jwt.encode({'user_id': user.id}, key=key, algorithm='HS256')
        return Response({'token': token})
    else:
        return Response({"message": 'These credentials are incorrect.'})
@api_view(['POST'])
def validation(request):
    token=request.POST['token']
    valid=jwt.decode(token,key=key,algorithms='HS256')
    return Response({'valid':valid})
