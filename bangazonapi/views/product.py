"""View module for handling requests about products"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Product, ProductType, Customer

class ProductSerializer(serializers.ModelSerializer):
  """JSON serializer for products"""
  class Meta:
    model = Product
    fields = "__all__"
    depth = 1
    
class ProductView(ViewSet):
  """Bangazon product View"""
  
  def retrieve(self, request, pk):
    """Handle GET single product"""
    try:
      product = Product.objects.get(pk=pk)
      serializer = ProductSerializer(product)
      return Response(serializer.data)
    
    except Product.DoesNotExist as exception:
      return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get all products"""
    products = Product.objects.all()
    
    id = request.query_params.get('id', None)
    if id is not None:
      products = products.filter(id=id)
      
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST requests for a single product"""
    
    product_type = ProductType.objects.get(id=request.data["product_type"])
    seller = Customer.objects.get(id=request.data["seller"])
    product = Product.objects.create(
      title = request.data["title"],
      cost = request.data["cost"],
      description = request.data["description"],
      quantity = request.data["quantity"],
      image = request.data["image"],
      product_type = product_type,
      seller = seller,
      )
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Handle PUT requests for products

    Returns:
        Response -- Empty body with 204 status code
    """

    product = Product.objects.get(pk=pk)
    product.title = request.data["title"]
    product.cost = request.data["cost"]
    product.description = request.data["description"]
    product.quantity = request.data["quantity"]
    product.image = request.data["image"]
    product.product_type = ProductType.objects.get(id=request.data["product_type"])
    product.seller = Customer.objects.get(id=request.data["seller"])
    
    product.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
