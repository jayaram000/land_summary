from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
from rest_framework.decorators import api_view
from .models import Land
from .serializers import LandSerializer
from django.db.models import Q
# Create your views here.

@api_view(['GET'])
def land_record(request):
    query = request.GET.get("query")

    search_result = Land.objects.filter(Q(parcel_id__icontains=query) | Q(plot_number__icontains=query) | Q(owner_name__icontains=query))

    if not search_result:
        return HttpResponse("No record found",status=404)

    serializer_data = LandSerializer(search_result,many=True).data

    html = render_to_string("summary.html",{"records":serializer_data})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="summary.pdf" '
    pisa.CreatePDF(html,dest=response)

    return response
