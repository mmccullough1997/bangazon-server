"""View module for handling requests about product orders"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import ProductOrder, Order, Product

class ProductOrderSerializer(serializers.ModelSerializer):
  """JSON serializer for payment types"""
  class Meta:
    model = ProductOrder
    fields = "__all__"
    depth = 1
    
class ProductOrderView(ViewSet):
  """Bangazon product order View"""
  
  def retrieve(self, request, pk):
    """Handle GET single product order"""
    try:
      product_order = ProductOrder.objects.get(pk=pk)
      serializer = ProductOrderSerializer(product_order)
      return Response(serializer.data)
    
    except ProductOrder.DoesNotExist as exception:
      return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get all product orders"""
    product_orders = ProductOrder.objects.all()
    
    id = request.query_params.get('id', None)
    if id is not None:
      product_orders = product_orders.filter(id=id)
      
    serializer = ProductOrderSerializer(product_orders, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST requests for a single payment type"""
    
    product = Product.objects.get(id=request.data["product"])
    order = Order.objects.get(id=request.data["order"])
    product_order = ProductOrder.objects.create(
      product = product,
      order = order,
      quantity = request.data["quantity"],
    )
    serializer = ProductOrderSerializer(product_order)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Handle PUT requests for product orders

    Returns:
        Response -- Empty body with 204 status code
    """

    product_order = ProductOrder.objects.get(pk=pk)
    product_order.product = Product.objects.get(id=request.data["product"])
    product_order.order = Order.objects.get(id=request.data["order"])
    product_order.quantity = request.data["quantity"]
    
    product_order.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    product_order = ProductOrder.objects.get(pk=pk)
    product_order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
