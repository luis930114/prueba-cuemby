from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'player', views.PlayerViewSet)

# URL's for create and get dataset, get and filter rows
urlpatterns = [
    path('team/', views.get_player),
    path('load/', views.load_players),
    # path('players?search=<str:search>/', views.find_players),
    path('players', views.find_players),
    path('', include(router.urls))
]