from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User


@api_view(["POST"])
def login(request):

    # buscar usuario por username
    user = get_object_or_404(User, username=request.data["username"])

    # validar password
    if not user.check_password(request.data["password"]):
        return Response(
            {"error": "Invalind password"}, status=status.HTTP_400_BAD_REQUEST
        )

    # creacion de token
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializers(instance=user)

    return Response(
        {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def register(request):
    # serializacion datos
    serializer = UserSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        # registro de ususario
        user = User.objects.get(username=serializer.data["username"])
        user.set_password(serializer.data["password"])
        user.save()

        # generacion de token
        token = Token.objects.create(user=user)
        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog(request):

    print(request.user)
    print(request.user.id)

    return Response(
        "You are login with {} ".format(request.user.username),
        status=status.HTTP_200_OK,
    )
