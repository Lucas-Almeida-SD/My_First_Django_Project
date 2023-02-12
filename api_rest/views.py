from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import User
from .serializers import UserSerializer


@api_view(["GET", "POST"])
def get_all_users(request: Request):
    if request.method == "GET":
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
