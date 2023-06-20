# No 404 page on route, change message shown - import into main urls.py and add path
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "You've reached the Summer Activities backend API."
    })