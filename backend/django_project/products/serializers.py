from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse 

class ProductSerializer(serializers.ModelSerializer):

    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name= 'product-detail',lookup_field="pk",)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = ['email','url','edit_url',"pk",'title','content','price','sale_price','my_discount']


    def get_my_discount(self,obj):
        return obj.get_discount()
    
    def get_edit_url(self,obj):

        request = self.context.get('request')
        if request is None:
            return None

        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)