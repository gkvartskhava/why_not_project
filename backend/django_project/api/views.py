# from django.http import JsonResponse,HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    instance =Product.objects.all().order_by('?').first()
    data = {}

    if instance:
        data = ProductSerializer(instance).data
    #     data = model_to_dict(instance, fields=['id','title', 'content', 'price','sale_price'])
    # else:
    #     pass
        return Response(data)
    # return HttpResponse(data, headers = {"content-type": "aplication/json"})