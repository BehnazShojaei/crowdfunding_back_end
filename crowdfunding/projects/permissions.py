from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):

      if request.method in permissions.SAFE_METHODS:
          return True
      return obj.owner == request.user
  
class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user
    
class IsSuperUser(BasePermission):
    """
    Custom permission that allows only superusers to delete users.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser