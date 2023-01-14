from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import ProductType

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"
class ProductTypeView(ViewSet):
    """product_type view"""
    def retrieve(self, request, pk):
        """Handle GET request for single product_type
        """
        try:
            product_type = ProductType.objects.get(pk=pk)
            serializer = ProductTypeSerializer(product_type)
            return Response(serializer.data)
        except ProductType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET request for all Product Types
        """
        product_types = ProductType.objects.all()
        
        id = request.query_params.get('id', None)
        if id is not None:
          product_types = product_types.filter(id=id)
      
        serializer = ProductTypeSerializer(product_types, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests to product types"""
        
        product_type = ProductType.objects.get(pk=pk)
        product_type.label = request.data["label"]
        product_type.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
      """Handle POST requests to product types"""
      
      product_type = ProductType.objects.create(label=request.data["label"])
      serializer = ProductTypeSerializer(product_type)
      return Response(serializer.data)

    def destroy(self, request, pk):
        product_type = ProductType.objects.get(pk=pk)
        product_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
