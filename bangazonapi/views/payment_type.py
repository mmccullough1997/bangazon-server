"""View module for handling requests about payment types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import PaymentType, Customer

class PaymentTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for payment types"""
  class Meta:
    model = PaymentType
    fields = "__all__"
    depth = 1
    
class PaymentTypeView(ViewSet):
  """Bangazon Payment type View"""
  
  def retrieve(self, request, pk):
    """Handle GET single payment type"""
    try:
      payment_type = PaymentType.objects.get(pk=pk)
      serializer = PaymentTypeSerializer(payment_type)
      return Response(serializer.data)
    
    except PaymentType.DoesNotExist as exception:
      return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get all payment types"""
    payment_types = PaymentType.objects.all()
    
    id = request.query_params.get('id', None)
    if id is not None:
      payment_types = payment_types.filter(id=id)
      
    payment_type_user = request.query_params.get('customer', None)
    if payment_type_user is not None:
      payment_types = payment_types.filter(customer=payment_type_user)
      
    serializer = PaymentTypeSerializer(payment_types, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST requests for a single payment type"""
    
    customer = Customer.objects.get(id=request.data["customer"])
    payment_type = PaymentType.objects.create(
      label = request.data["label"],
      account_number = request.data["account_number"],
      customer = customer,
      )
    serializer = PaymentTypeSerializer(payment_type)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Handle PUT requests for payment_types

    Returns:
        Response -- Empty body with 204 status code
    """

    payment_type = PaymentType.objects.get(pk=pk)
    payment_type.label = request.data["label"]
    payment_type.account_number = request.data["account_number"]
    payment_type.customer = Customer.objects.get(id=request.data["customer"])
    
    payment_type.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    payment_type = PaymentType.objects.get(pk=pk)
    payment_type.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
