from django.db import models


# Model for player description in database
class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    @classmethod
    def create(cls, name, position, nationality, team):
        player = cls(name=name, position=position, nationality=nationality, team=team)
        player.save()
        return player

    def __str__(self):
        return self.name
