"""View module for handling requests about orders"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Order, PaymentType, Customer, ProductOrder, Product
from .product_order import ProductOrderSerializer
from .product import ProductSerializer
from .customer import CustomerSerializer


class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for Orders"""
  class Meta:
    model = Order
    fields = ('id', 'cost', 'payment_type', 'customer', 'date_placed', 'product_orders_on_order')
    depth = 2
    
class OrderView(ViewSet):
  """Bangazon Order View"""
  
  def retrieve(self, request, pk):
    """Handle GET single order"""
    try:
      order = Order.objects.get(pk=pk)
      
      product_orders = ProductOrder.objects.filter(order=order.id)
      product_orders_on_order = []
      
      for product_order in product_orders:
        try:
          product_orders_on_order_dict = {}
          product_orders_on_order_dict['id'] = product_order.id
          
          product = Product.objects.get(id=product_order.product.id)
          product_serialized = ProductSerializer(product)
          product_orders_on_order_dict['product'] = product_serialized.data
          
          
          product_orders_on_order_dict['customer'] = product_order.customer.id
          product_orders_on_order_dict['quantity'] = product_order.quantity
          product_orders_on_order.append(product_orders_on_order_dict)
        except:
          pass
        
      order.product_orders_on_order = product_orders_on_order
      
        
      serializer = OrderSerializer(order)
      return Response(serializer.data)
    
    except Order.DoesNotExist as exception:
      return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get all orders"""
    orders = Order.objects.all()
    
    id = request.query_params.get('id', None)
    if id is not None:
      orders = orders.filter(id=id)
      
    orders_by_customer = request.query_params.get('customer', None)
    if orders_by_customer is not None:
      orders = orders.filter(customer=orders_by_customer)
      
    for order in orders:
      product_orders = ProductOrder.objects.filter(order=order.id)
      product_orders_on_order = []
      
      for product_order in product_orders:
        try:
          product_orders_on_order_dict = {}
          product_orders_on_order_dict['id'] = product_order.id
          
          product = Product.objects.get(id=product_order.product.id)
          product_serialized = ProductSerializer(product)
          product_orders_on_order_dict['product'] = product_serialized.data
          
          product_orders_on_order_dict['customer'] = product_order.customer.id
          product_orders_on_order_dict['quantity'] = product_order.quantity
          product_orders_on_order.append(product_orders_on_order_dict)
        except:
          pass
        order.product_orders_on_order = product_orders_on_order
      
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST requests for a single order"""
    
    customer = Customer.objects.get(id=request.data["customer"])
    payment_type = PaymentType.objects.get(id=request.data["payment_type"])
    order = Order.objects.create(
      cost = request.data["cost"],
      payment_type = payment_type,
      customer = customer,
      date_placed = request.data["date_placed"]
      )
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Handle PUT requests for orders

    Returns:
        Response -- Empty body with 204 status code
    """

    order = Order.objects.get(pk=pk)
    order.cost = request.data["cost"]
    order.payment_type = PaymentType.objects.get(id=request.data["payment_type"])
    order.date_placed = request.data["date_placed"]
    order.customer = Customer.objects.get(id=request.data["customer"])
    
    order.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
