from rest_framework import authentication,generics,mixins,permissions

from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.mixins import (StaffEditorPermissionMixin,UserQuerySetMixin)

# from ..api.permissions import IsStaffEditorPermission

from django.shortcuts import get_object_or_404


# from api.authentication import TokenAuthentication



class ProductListCreateApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # authentication_classes = [authentication.SessionAuthentication,TokenAuthentication,]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user = self.request.user,content = content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request= self.request

    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()

    #     # print(request.user)
    #     return qs.filter(user=request.user)


class ProductDetailApiView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    # permission_classes = [IsStaffEditorPermission]

    # lookup_field = 'pk'

# class ProductListApiView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



class ProductUpdateApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    # permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        return super().perform_update(serializer)
    

class ProductDeleteApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_destroy(self, instance):
        
        super().perform_destroy(instance)


class ProdductMixinView(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self,request, *args, **kwargs):
        # print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     # serializer.save(user=self.request.user)
        
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = "pushing all CRUD operations in single view "
    #     serializer.save(content = content)
    


@api_view(['GET','POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj, many=False).data

            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
                serializer.save(content = content)

            return Response(serializer.data)
        return Response({"invlid":"not good data"},status=400)
    