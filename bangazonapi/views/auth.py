from rest_framework.decorators import api_view
from rest_framework.response import Response
from bangazonapi.models import Customer


@api_view(['POST'])
def check_customer(request):
    '''Checks to see if customer exists

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the customer object or None if no customer is found
    try: 
              
        customer = Customer.objects.get(uid=uid)

    # If authentication was successful, respond with their token
        data = {
            'id': customer.id,
            'uid': customer.uid,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'date_registered': customer.date_registered,
            'bio': customer.bio,
            'image': customer.image,
        }
        return Response(data)
    except:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_customer(request):
    '''Handles the creation of a new customer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    # Now save the customer info in the banganapi_customer table
    customer = Customer.objects.create(
        uid=request.data['uid'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        date_registered = request.data['date_registered'],
        bio = request.data['bio'],
        image = request.data['image']
    )

    # Return the customer info to the client
    data = {
            'id': customer.id,
            'uid': customer.uid,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'date_registered': customer.date_registered,
            'bio': customer.bio,
            'image': customer.image,
        }
    return Response(data)
