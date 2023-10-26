from .permissions import TokenHasScope1, TokenHasScope2

from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import (
    OAuth2Authentication,
    TokenHasReadWriteScope,
)

@extend_schema(
    responses={
        200: inline_serializer(
            name="ExampleOutput",
            fields={
                "message": serializers.CharField()
            }
        )
    }
)
class BookView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope1 | TokenHasScope2]

    def get(self, request):
        return Response({"message": "success"}, 200)
