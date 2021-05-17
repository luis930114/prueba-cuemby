from api.models import Player
import requests
from django.core.paginator import Paginator


def get_load_player_fifa():
    """
        load data players to api fifa
    """
    for i in range(8):
        get_player_info(i)
    return True


# get_player_info allows get player base information by name
def get_player_info(page):
    url_info = "http://www.easports.com/fifa/ultimate-team/api/fut/item?page={0}".format(page)
    r_info = requests.get(url_info)
    data_info = r_info.json()
    players = data_info['items']
    for player in players:
        name = player['name']
        position = player['position']
        nationality = player['nation']['name']
        team = player['club']['name']
        if not get_register_players(name):
            Player.create(name, position, nationality, team)


def get_register_players(name):
    """ return players in database """
    return Player.objects.filter(name=name)


def get_name_player(name):
    """ get the occurrences of a string """
    return Player.objects.filter(name__icontains=name).order_by('id')


