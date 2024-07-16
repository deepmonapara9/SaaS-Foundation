from django.http import HttpResponse
from visits.models import PageVisit 

def home_page_view(request):
    return HttpResponse("<h1>Hola!!</h1>")