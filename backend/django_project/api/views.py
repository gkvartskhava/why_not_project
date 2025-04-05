from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    # request --> HttpRequest --> django
    # request.body
    print(request.GET)
    print(request.POST)

    data = {}
    body = request.body
    try:
        data=json.loads(body)
    except:
        pass
    
    print(data)
    # print(body)
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) # request.META
    data['content_type'] = request.content_type
    

    
    return JsonResponse(data)