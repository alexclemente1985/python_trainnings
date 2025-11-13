from rest_framework import serializers
from apps.app_antiga.models import Teste


class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = ('id','descricao')