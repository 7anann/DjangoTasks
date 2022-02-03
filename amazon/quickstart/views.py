from django.shortcuts import render

# Create your views here.
from affairs.models import students
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = students.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET','PUT', 'DELETE'])
def stud_details(request, pk):

    try:
        stud = students.objects.get(id=pk)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(stud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)