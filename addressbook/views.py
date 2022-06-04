from .models import Address
from .serializers import AddressSerializer
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddressApiView(APIView):
    def get(self, request, pk, format=None):
        ad = Address.objects.filter(pk = pk).first()
        if ad:
            serializer = AddressSerializer(ad)
            return Response(serializer.data)
        return Response('No such address in address book exists kindly check id/pk')

    def post(self, request,pk, format=None):
        serializer = AddressSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request,pk, format=None):
        obj = Address.objects.filter(pk=pk).first()
        if obj:    
            serializer = AddressSerializer(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data
                )
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response('No such address in address book exists kindly check id/pk')

    def delete(self,request,pk, format=None):
        obj = Address.objects.filter(pk=pk).first()
        obj.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class NearByAddressApiView(APIView):
    def get(self, request, format=None):
        aid = request.GET.get('aid',None)
        print(aid)
        ad = Address.objects.filter(id=aid).first()
        if ad:
            obj = Address.objects.filter(latitude__lte=ad.latitude+1,latitude__gte=ad.latitude-1,longitude__lte=ad.longitude+1,longitude__gte=ad.longitude-1)
            print(obj)
            if obj:
                serializer = AddressSerializer(obj,many=True)
                return Response(serializer.data)
        return Response('No such address in address book exists with nearby coordinates')

class AllAddressApiView(APIView):
    def get(self, request, format=None):
        obj = Address.objects.all().order_by('city')
        serializer = AddressSerializer(obj,many=True)
        return Response(
            data=serializer.data
        )