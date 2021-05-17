from rest_framework.response import Response
from rest_framework import status
from api.models import Player
from api.serializers import PlayerSerializer
from rest_framework.views import APIView
from api.functions import get_load_player_fifa, get_name_player
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import permissions
from fifaApi.permission import SetXApiKey
from rest_framework_api_key.permissions import HasAPIKey


# Endpoint for get all players information
class GetPlayer(APIView):
    permission_classes = [SetXApiKey, HasAPIKey]
    player_serializer = PlayerSerializer

    def post(self, request):
        try:

            if "name" in request.data:
                players = Player.objects.filter(team__iexact=request.data['name'])
                page = request.data['page']

                p = Paginator(players, 10)
                try:
                    players = p.page(page)
                except PageNotAnInteger:
                    players = p.page(1)
                except EmptyPage:
                    players = p.page(p.num_pages)
                response = self.player_serializer(players, many=True)
                if page <= p.num_pages:
                    return Response({
                        'page': page,
                        'totalPages': p.num_pages,
                        'totalItem': p.count,
                        'Players': response.data
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'message': "page is greater than number of pager pages"}, status=status.HTTP_404_NOT_FOUND)

        except Player.DoesNotExist:
            message = 'team not found'
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


get_player = GetPlayer.as_view()


class LoadPlayers(APIView):

    def get(self, request):
        get_load_player_fifa()
        return Response({'message': "data loaded succesfully"}, status=status.HTTP_201_CREATED)


load_players = LoadPlayers.as_view()


class FindPlayers(APIView):
    player_serializer = PlayerSerializer

    def get(self, request):
        # import pdb; pdb.set_trace()
        search = request.query_params["search"]
        order = request.query_params["order"] if "order" in request.query_params else "asc"
        result = get_name_player(search)
        response = self.player_serializer(result, many=True)
        return Response(response.data, status=status.HTTP_200_OK)


find_players = FindPlayers.as_view()


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all().order_by("id")
    serializer_class = PlayerSerializer
    filter_fields = ("name",)
    permission_classes = [SetXApiKey, HasAPIKey]

    def get_queryset(self):
        search = self.request.query_params.get("search",'')
        queryset = get_name_player(search)
        return queryset
