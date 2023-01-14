"""bangazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path

from bangazonapi.views import register_customer, check_customer, CustomerView, OrderView, PaymentTypeView, ProductOrderView, ProductTypeView, ProductView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'orders', OrderView, 'order')
router.register(r'paymenttypes', PaymentTypeView, 'paymenttype')
router.register(r'productorders', ProductOrderView, 'productorder')
router.register(r'producttypes', ProductTypeView, 'producttype')
router.register(r'products', ProductView, 'product')

urlpatterns = [
    path('register', register_customer),
    path('checkuser', check_customer),
    path('admin/', admin.site.urls),
    # Requests to http://localhost:8000/checkuser will be routed to the login_user function
    path('', include(router.urls)),
]
