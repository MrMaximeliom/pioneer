from rest_framework import permissions
class IsSystemBackEndUser(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_permission(self, request, view):

        # if request.method in permissions.SAFE_METHODS:
        #     return False
        # else:
        if not request.user.is_anonymous:
            if request.user.user_role == 4 or request.user.admin:
                return True
            else:
                return False


class IsAnonymousUser(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):

        # if request.method in permissions.SAFE_METHODS:
        #     return False
        # else:
        if request.user.is_anonymous or request.user.admin:
            return True
        else:
            return False
