from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import User
from .serializers import UserSerializer


@api_view(["GET"])
def get_all_users(request: Request):
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_user(request: Request):
    new_user = request.data

    serializer = UserSerializer(data=new_user)
    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(
        data={"message": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["PUT"])
def get_user_by_id(request: Request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(
            data={"message": "Usuário não encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            data={"message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
