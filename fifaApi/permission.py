from django.conf import settings
from decouple import config

from rest_framework.permissions import BasePermission


class SetXApiKey(BasePermission):
    def has_permission(self, request, view):
        request.META['HTTP_X_API_KEY'] = config('X-API-KEY')
        return True
