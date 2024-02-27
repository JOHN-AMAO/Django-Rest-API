
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET", "POST"])
def api_home(request):
    response = request.body
    return Response(response)


