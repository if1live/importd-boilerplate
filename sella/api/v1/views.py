#-*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from . import serializers
from importd import d


@d('/v1/users/<int:pk>', name='v1.user_detail')
@d('/v1/users/<int:pk>.<slug:format>', name='v1.user_detail')
@api_view(['GET'])
def user_detail(request, pk, format=None):
    pk = int(pk)

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

