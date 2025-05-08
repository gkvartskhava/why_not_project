from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from .client import perform_search

from  . import client



class SearchOldListView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = request.user.username if request.user.is_authenticated else None
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None

        if not query:
            return Response('', status=400)

        raw_result = perform_search(query, tags=tag, user=user, public=public)

        # If using multi-index search, extract hits from first result
        try:
            hits = raw_result['results'][0]['hits']
        except (KeyError, IndexError, TypeError):
            return Response({'error': 'Invalid response structure from Algolia'}, status=500)

        return Response(hits)

# class SearchOldListView(generics.GenericAPIView):
    
#     def get(self, request, *args, **kwargs):
#         user = None
#         if request.user.is_authenticated:
#             user = request.user.username
#         query = request.GET.get('q')
#         public = str(request.GET.get('public')) != "0"
#         tag = request.GET.get('tag') or None
#         # print(query,user,public)
#         if not query:
#             return Response('', status=400)
#         results = client.perform_search(query,tags=tag , user = user, public = public)
#         return Response(results)


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs =  super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user

            results = qs.search(q, user = user)
        return results
