from urllib import request

from django.contrib.messages import error, success, warning
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class UserIsOwnerMixin(object):
    owner_field = "creator"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if getattr(obj, self.owner_field) != request.user:
            redirect("login")
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class HiMessageMixin:
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        success(request, f"Привіт, {request.user.username}!")
        return super().dispatch(request, *args, **kwargs)
