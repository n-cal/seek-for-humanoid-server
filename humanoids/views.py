from rest_framework.decorators import api_view
from rest_framework.response import Response
from humanoids.models import Humanoid

@api_view(['GET'])
def all_countries(request):
    countries = list(set(Humanoid.objects.values_list('country', flat=True)))
    countries.sort()
    return Response(countries)