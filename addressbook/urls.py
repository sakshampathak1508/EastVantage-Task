from django.urls import path

from .views import AddressApiView,NearByAddressApiView,AllAddressApiView

urlpatterns = [
  path('', AllAddressApiView.as_view(), name='all-address'),
  path('nearby-address/', NearByAddressApiView.as_view(), name='nearby-address'),
  path('address/<int:pk>', AddressApiView.as_view(), name='address-by-id'),
]
