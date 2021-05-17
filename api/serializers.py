from api.models import Player
from rest_framework.serializers import ModelSerializer


# Serializer class for Player
class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = ('name', 'position', 'nationality', 'team')



