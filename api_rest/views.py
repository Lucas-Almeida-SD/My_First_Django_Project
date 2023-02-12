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

    if request.method == "POST":
        new_user = request.data

        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_user(request, id):
    if request.method == "PUT":
        try:
            find_user = User.objects.get(pk=id)
        except Exception:
            Response(status=status.HTTP_404_NOT_FOUND)

        update = request.data
        serializer = UserSerializer(find_user, data=update)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(status=status.HTTP_400)

    return Response(status=status.HTTP_400_BAD_REQUEST)
