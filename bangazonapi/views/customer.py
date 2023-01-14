"""View module for handling requests about customers"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
  """JSON serializer for Customers"""
  class Meta:
    model = Customer
    fields = ('id', 'uid', 'first_name', 'last_name', 'date_registered', 'bio', 'image')
    
class CustomerView(ViewSet):
  """Bangazon Customer View"""
  
  def retrieve(self, request, pk):
    """Handle GET single customer"""
    try:
      customer = Customer.objects.get(pk=pk)
      serializer = CustomerSerializer(customer)
      return Response(serializer.data)
    
    except Customer.DoesNotExist as exception:
      return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get all customers"""
    customers = Customer.objects.all()
    
    id = request.query_params.get('id', None)
    if id is not None:
      customers = customers.filter(id=id)
      
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Handle PUT requests for customers

    Returns:
        Response -- Empty body with 204 status code
    """

    customer = Customer.objects.get(pk=pk)
    customer.first_name = request.data["first_name"]
    customer.last_name = request.data["last_name"]
    customer.date_registered = request.data["date_registered"]
    customer.bio = request.data["bio"]
    customer.image = request.data["image"]
    
    customer.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
