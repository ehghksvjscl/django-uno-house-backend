from rest_framework.exceptions import NotAuthenticated, ParseError, PermissionDenied


def check_authentication(request):
    if not request.user.is_authenticated:
        raise NotAuthenticated


def check_host(request, room):
    if room.host.pk != request.user.pk:
        raise PermissionDenied("You are not the host of this room")
