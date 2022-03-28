from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from movie_app.serializers import ReviewSerializers
from movie_app.models import Review


@api_view(['POST'])
def authorization(request):
    if request.method == 'POST':
        username = request.data.get('username')  # admin
        password = request.data.get('password')  # 123
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)


from django.contrib.auth.models import User


@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username, password=password)
        return Response(data={'message': 'User created'},
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_reviews(request):
    reviews = Review.objects.filter(author=request.user)
    serializer = ReviewSerializers(reviews, many=True)
    return Response(data=serializer.data)
