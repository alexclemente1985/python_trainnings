from apps.app_antiga.api.serializers import TesteSerializer
from apps.app_antiga.models import Teste
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TesteViewSet(viewsets.ModelViewSet):
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)