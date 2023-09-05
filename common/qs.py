from rest_framework.exceptions import ParseError

from categories.models import Category
from rooms.models import Amenity, Room


def get_room_category(request):
    try:
        category = Category.objects.get(pk=request.data.get("category_id"))
    except Category.DoesNotExist:
        raise ParseError("category does not exist")

    if category.kind != Category.CategoryKind.rooms:
        raise ParseError("category must be a room category")

    return category


def add_room_amenities(request, room: Room) -> Room:
    amenity_ids = request.data.get("amenities", [])
    if not isinstance(amenity_ids, list):
        raise ParseError("amenities must be a list")

    for amenity_id in amenity_ids:
        try:
            amenity = Amenity.objects.get(id=amenity_id)
            room.amenities.add(amenity)
        except Amenity.DoesNotExist:
            raise ParseError(f"Amenity {amenity_id} does not exist")

    return room
