from django.http import JsonResponse
from .models import Epreuve

def epreuves_list(request):
    epreuves = Epreuve.objects.all().values('discipline', 'nom', 'description', 'date_heure', 'lieu')
    return JsonResponse(list(epreuves), safe=False)